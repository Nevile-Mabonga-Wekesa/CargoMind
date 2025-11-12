# app/workers/route_optimization.py
from app.core.celery_app import celery
from app.core.database import SessionLocal
from app.models.route import Route
from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape
from shapely.geometry import LineString

import random

@celery.task(name="app.workers.route_optimization.compute_routes")
def compute_routes():
    db: Session = SessionLocal()
    try:
        # Fetch active vehicles and deliveries (pseudo-code)
        # Replace with actual queries
        active_vehicles = [{"vehicle_id": 1, "deliveries": [101, 102, 103]}]

        for vehicle in active_vehicles:
            deliveries = vehicle["deliveries"]
            # Simulate route calculation
            coords = [(random.uniform(-1.3, -1.2), random.uniform(36.8, 36.9)) for _ in deliveries]
            linestring = LineString(coords)
            total_distance = sum(random.uniform(1, 10) for _ in deliveries)
            estimated_time = sum(random.uniform(5, 15) for _ in deliveries)

            route = Route(
                vehicle_id=vehicle["vehicle_id"],
                delivery_sequence=",".join(map(str, deliveries)),
                total_distance=total_distance,
                estimated_time=estimated_time,
                geometry=from_shape(linestring, srid=4326)
            )
            db.add(route)
        db.commit()
    finally:
        db.close()
