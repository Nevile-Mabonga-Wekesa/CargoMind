# app/api/routes/routes.py
from fastapi import APIRouter, Depends
from app.core.auth import get_current_user
from app.workers.route_optimization import compute_routes

router = APIRouter(prefix="/routes", tags=["Routes"])

@router.post("/optimize")
def optimize_routes(current_user: dict = Depends(get_current_user)):
    if current_user["role"] not in ["dispatcher", "admin"]:
        return {"error": "Unauthorized"}
    compute_routes.delay()
    return {"status": "success", "message": "Route optimization task queued"}
