# app/models/telemetry.py
from sqlalchemy import Column, Integer, Float, DateTime, String, Index
from sqlalchemy.sql import func
from geoalchemy2 import Geometry
from app.core.database import Base

class Telemetry(Base):
    __tablename__ = "telemetry"
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, nullable=False, index=True)
    lat = Column(Float, nullable=False)
    lon = Column(Float, nullable=False)
    speed = Column(Float, nullable=True)
    heading = Column(Float, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    geom = Column(Geometry(geometry_type="POINT", srid=4326), nullable=False)

# useful index for spatial queries (create via migration or raw SQL)
# CREATE INDEX telemetry_geom_gist ON telemetry USING GIST (geom);
