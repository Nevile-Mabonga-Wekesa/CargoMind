# app/workers/persist.py
from datetime import datetime
from app.core.celery_app import celery
from app.core.database import SessionLocal
from app.models.telemetry import Telemetry
from sqlalchemy import insert
from geoalchemy2.shape import from_shape
from shapely.geometry import Point

BATCH_SIZE = 200  # tune per load
BATCH_WINDOW_SEC = 2  # group short bursts (optional)

@celery.task(bind=True, name="persist_location", acks_late=True)
def persist_location(self, payload):
    """
    payload: dict with keys vehicle_id, lat, lon, speed, heading, timestamp (iso str)
    Called for every update. This task performs single insert.
    For high throughput, consider a batching aggregator task or use Redis stream and consumer reading multiple entries.
    """
    session = SessionLocal()
    try:
        ts = payload.get("timestamp")
        if ts:
            ts = datetime.fromisoformat(ts)
        else:
            ts = datetime.utcnow()

        point = from_shape(Point(payload["lon"], payload["lat"]), srid=4326)

        telemetry = Telemetry(
            vehicle_id=int(payload["vehicle_id"]),
            lat=float(payload["lat"]),
            lon=float(payload["lon"]),
            speed=float(payload.get("speed") or 0),
            heading=float(payload.get("heading") or 0),
            timestamp=ts,
            geom=point
        )

        session.add(telemetry)
        session.commit()
    except Exception as e:
        session.rollback()
        raise self.retry(exc=e, countdown=2 ** self.request.retries, max_retries=5)
    finally:
        session.close()
