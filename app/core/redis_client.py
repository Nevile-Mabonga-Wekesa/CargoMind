# app/core/redis_client.py
import redis
import json
from app.core.config import settings
from app.workers.persist import persist_location
r = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True
)

def save_vehicle_location(location: dict):
    key = f"vehicle:{location['vehicle_id']}"
    r.hset(key, mapping={
        "lat": location["lat"],
        "lon": location["lon"],
        "speed": location["speed"],
        "heading": location["heading"],
        "timestamp": location["timestamp"].isoformat()
    })
    r.publish("vehicle_updates", json.dumps(location))

    # enqueue persistence asynchronously
    try:
        persist_location.delay(location)
    except Exception:
        # fail-open: don't block API if Celery temporarily unavailable
        # optionally push to a Redis list for a fallback consumer
        r.rpush("telemetry_fallback_queue", json.dumps(location))

def get_vehicle_location(vehicle_id: int):
    key = f"vehicle:{vehicle_id}"
    data = r.hgetall(key)
    if not data:
        return None
    return {
        "vehicle_id": vehicle_id,
        "lat": float(data["lat"]),
        "lon": float(data["lon"]),
        "speed": float(data["speed"]),
        "heading": float(data["heading"]),
        "timestamp": data["timestamp"]
    }
