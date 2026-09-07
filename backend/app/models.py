from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
from app.database import Base

class DiseaseDetection(Base):
    """Stores history of crop image analysis requests made by farmers."""
    __tablename__ = "disease_detections"

    id = Column(Integer, primary_key=True, index=True)
    crop_type = Column(String, index=True)
    image_path = Column(String)
    location = Column(String)
    predicted_disease = Column(String)
    confidence = Column(Float)
    health_status = Column(String)
    language = Column(String, default="en")
    created_at = Column(DateTime, default=datetime.utcnow)

class Ticket(Base):
    """Stores expert-support tickets raised by farmers."""
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    crop_type = Column(String, index=True)
    image_path = Column(String)
    location = Column(String)
    problem_description = Column(Text)
    language = Column(String, default="en")
    ai_result = Column(String, nullable=True)
    ai_confidence = Column(Float, nullable=True)
    status = Column(String, default="Pending Review")  # Pending Review, Under Review, Resolved, etc.
    expert_response = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)