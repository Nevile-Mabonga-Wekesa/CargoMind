from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import auth
from app.core.database import engine, Base
from app.models.models import Admin, Dispatcher, Driver, Contact

app = FastAPI(title="Real-Time Logistics API")

app.include_router(auth.router)
Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return {"status": "ok", "message": "Real-Time Logistics API running"}

# To run locally: uvicorn app.main:app --reload
