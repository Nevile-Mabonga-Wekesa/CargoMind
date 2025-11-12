# app/models/routes.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from geoalchemy2 import Geometry
from app.core.database import Base
from datetime import datetime

class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, nullable=False)
    delivery_sequence = Column(String, nullable=False)  # comma-separated delivery IDs
    total_distance = Column(Float, nullable=False)
    estimated_time = Column(Float, nullable=False)  # in minutes
    geometry = Column(Geometry("LINESTRING", srid=4326), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
