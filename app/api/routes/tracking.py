# app/api/routes/tracking.py
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.vehicle import VehicleLocationUpdate
from app.core.redis_client import save_vehicle_location
from app.core.auth import get_current_user

router = APIRouter(prefix="/track", tags=["Tracking"])

@router.post("/update_location")
async def update_location(
    payload: VehicleLocationUpdate,
    current_user: dict = Depends(get_current_user)
):
    if current_user["role"] != "driver":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only drivers can update location."
        )

    save_vehicle_location(payload.dict())
    return {"status": "success", "vehicle_id": payload.vehicle_id}
