from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid
from app.core.database import Base

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

class Admin(Base):
    __tablename__ = "admins"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone_number = Column(String(20))
    employee_id = Column(String(50), unique=True)
    contact_id = Column(Integer, ForeignKey("contacts.id", ondelete="SET NULL"))
    role = Column(String(50), default="admin")
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    contact = relationship("Contact")

class Dispatcher(Base):
    __tablename__ = "dispatchers"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone_number = Column(String(20))
    station_name = Column(String(100))
    contact_id = Column(Integer, ForeignKey("contacts.id", ondelete="SET NULL"))
    role = Column(String(50), default="dispatcher")
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    contact = relationship("Contact")

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(150), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone_number = Column(String(20))
    license_number = Column(String(50), unique=True)
    contact_id = Column(Integer, ForeignKey("contacts.id", ondelete="SET NULL"))
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    contact = relationship("Contact")
