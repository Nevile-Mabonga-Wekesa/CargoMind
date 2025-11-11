from fastapi import FastAPI, HTTPException, Depends
from app.core.config import settings
from app.api.routes import auth
from app.core.database import engine, Base
from app.models.models import Admin, Dispatcher, Driver, Contact
from sqlalchemy import Column, Integer, String, create_engine
from pydantic import BaseModel
from app.api.routes import tracking
from app.api.routes import tracking, websocket_tracking

app = FastAPI(title="Real-Time Logistics API")

app.include_router(tracking.router)
app.include_router(auth.router, prefix="/auth")
app.include_router(websocket_tracking.router)

Base.metadata.create_all(bind=engine)
# app/main.py
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "postgresql://postgres:password@localhost:5432/fleet_system"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

Base.metadata.create_all(bind=engine)

class RegisterRequest(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/auth/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(username=data.username, password=data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered"}

@app.post("/auth/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.password != data.password:
        raise HTTPException(status_code=401, detail="Invalid password")
    return {"message": "Login successful"}



@app.get("/")
def root():
    return {"status": "ok", "message": "Real-Time Logistics API running"}

# To run locally: uvicorn app.main:app --reload
