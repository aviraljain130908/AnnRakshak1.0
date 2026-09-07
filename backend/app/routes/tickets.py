import os
import uuid
from typing import Optional, List
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Ticket
from app.schemas import TicketResponse, TicketUpdate
from app.services.image_preprocessing import validate_and_preprocess_image
from app.services.disease_model import disease_model_instance

router = APIRouter(prefix="/tickets", tags=["Farmer Support Tickets"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("", response_model=TicketResponse)
async def create_ticket(
    image: UploadFile = File(...),
    crop_type: str = Form(...),
    location: str = Form(...),
    problem_description: str = Form(...),
    language: str = Form("en"),
    db: Session = Depends(get_db)
):
    """Farmer creates an expert support ticket with image and problem details."""
    # Process crop image
    processed_image = await validate_and_preprocess_image(image)
    
    file_id = f"ticket_{uuid.uuid4().hex}_{image.filename}"
    file_path = os.path.join(UPLOAD_DIR, file_id)
    processed_image.save(file_path)

    # Automatic AI pre-screening to assist expert evaluation
    ai_output = disease_model_instance.predict(processed_image)
    ai_pred = ai_output["prediction"]
    ai_conf = ai_output["confidence"]

    # Flag high confidence serious issues as Urgent / Needs Expert Attention
    initial_status = "Needs Expert Attention" if ai_conf >= 0.85 else "Pending Review"

    ticket = Ticket(
        crop_type=crop_type,
        image_path=file_path,
        location=location,
        problem_description=problem_description,
        language=language,
        ai_result=ai_pred,
        ai_confidence=ai_conf,
        status=initial_status
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    return ticket

@router.get("", response_model=List[TicketResponse])
def get_tickets(
    status: Optional[str] = None,
    crop: Optional[str] = None,
    location: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Expert Dashboard: List and filter tickets."""
    query = db.query(Ticket)
    if status:
        query = query.filter(Ticket.status == status)
    if crop:
        query = query.filter(Ticket.crop_type == crop)
    if location:
        query = query.filter(Ticket.location == location)
        
    return query.order_by(Ticket.created_at.desc()).all()

@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket_detail(ticket_id: int, db: Session = Depends(get_db)):
    """Retrieve full ticket record for expert review."""
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@router.put("/{ticket_id}", response_model=TicketResponse)
def update_ticket(
    ticket_id: int,
    payload: TicketUpdate,
    db: Session = Depends(get_db)
):
    """Agriculture officer updates status or adds resolution feedback."""
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    if payload.status:
        ticket.status = payload.status
    if payload.expert_response:
        ticket.expert_response = payload.expert_response

    db.commit()
    db.refresh(ticket)
    return ticket