# app/schemas/vehicle.py
from pydantic import BaseModel, Field
from datetime import datetime

class VehicleLocationUpdate(BaseModel):
    vehicle_id: int = Field(..., example=101)
    lat: float = Field(..., ge=-90.0, le=90.0, example=-1.2921)
    lon: float = Field(..., ge=-180.0, le=180.0, example=36.8219)
    speed: float = Field(..., ge=0.0, example=45.5)  # km/h
    heading: float = Field(..., ge=0.0, le=360.0, example=180.0)  # degrees
    timestamp: datetime = Field(default_factory=datetime.utcnow)
