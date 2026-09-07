import os
import uuid
from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import DiseaseDetection
from app.schemas import DiseaseDetectionResponse, AlternativePrediction
from app.services.image_preprocessing import validate_and_preprocess_image
from app.services.disease_model import disease_model_instance
from app.utils.helpers import get_advisory, map_label_to_advisory_key

router = APIRouter(prefix="/disease", tags=["Disease Detection"])

CONFIDENCE_THRESHOLD = float(os.getenv("CONFIDENCE_THRESHOLD", "0.60"))
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/detect", response_model=DiseaseDetectionResponse)
async def detect_crop_disease(
    image: UploadFile = File(...),
    crop_type: str = Form(...),
    location: str = Form(...),
    language: str = Form("en"),
    db: Session = Depends(get_db)
):
    """
    Main disease detection API:
    - Preprocesses and validates image
    - Runs AI model with crop-type filtering
    - Returns top prediction + top-3 alternatives
    - Maps result to localized multilingual advisory
    - Saves history to SQLite
    """
    # 1. Preprocess & Validate Image
    processed_image = await validate_and_preprocess_image(image)

    # 2. Save local copy of the preprocessed file
    file_id = f"{uuid.uuid4().hex}_{image.filename}"
    file_path = os.path.join(UPLOAD_DIR, file_id)
    processed_image.save(file_path)

    # 3. Predict via AI Model (with crop-type filtering)
    model_output = disease_model_instance.predict(processed_image, crop_type=crop_type)
    raw_pred = model_output["prediction"]
    confidence = model_output["confidence"]
    alternatives_raw = model_output.get("alternatives", [])

    # 4. Map prediction to advisory key and determine health status
    if confidence >= CONFIDENCE_THRESHOLD:
        advisory_key = map_label_to_advisory_key(raw_pred)
        result_title = raw_pred

        if advisory_key in ("healthy", "tomato_healthy", "potato_healthy", "corn_healthy"):
            health_status = "Healthy"
        else:
            health_status = "Attention needed"
            # Disease detected but not in our advisory dictionary — use generic advice
            # instead of showing the "uncertain diagnosis" message
            if advisory_key == "uncertain":
                advisory_key = "generic_disease"
    else:
        advisory_key = "uncertain"
        result_title = "Uncertain"
        health_status = "Expert review recommended"

    # 5. Fetch localized advisory
    advisory = get_advisory(advisory_key, lang=language)

    # 6. Build alternatives list for response
    alternatives = [
        AlternativePrediction(
            label=alt["label"],
            confidence=round(alt["confidence"] * 100, 1)
        )
        for alt in alternatives_raw
    ]

    # 7. Persist record to database
    db_record = DiseaseDetection(
        crop_type=crop_type,
        image_path=file_path,
        location=location,
        predicted_disease=result_title,
        confidence=confidence,
        health_status=health_status,
        language=language
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)

    return DiseaseDetectionResponse(
        id=db_record.id,
        crop=crop_type,
        result=result_title,
        confidence=round(confidence * 100, 1),
        status=health_status,
        message=advisory["message"],
        basic_advice=advisory["basic_advice"],
        treatment=advisory.get("treatment"),
        language=language,
        image_path=file_path,
        alternatives=alternatives
    )


@router.get("/{detection_id}", response_model=DiseaseDetectionResponse)
def get_detection_by_id(detection_id: int, db: Session = Depends(get_db)):
    """Fetch stored detection record by ID."""
    record = db.query(DiseaseDetection).filter(DiseaseDetection.id == detection_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Detection record not found")

    if record.predicted_disease == "Uncertain":
        advisory_key = "uncertain"
    else:
        advisory_key = map_label_to_advisory_key(record.predicted_disease)

    advisory = get_advisory(advisory_key, lang=record.language)

    return DiseaseDetectionResponse(
        id=record.id,
        crop=record.crop_type,
        result=record.predicted_disease,
        confidence=round(record.confidence * 100, 1),
        status=record.health_status,
        message=advisory["message"],
        basic_advice=advisory["basic_advice"],
        treatment=advisory.get("treatment"),
        language=record.language,
        image_path=record.image_path,
        alternatives=[]
    )
