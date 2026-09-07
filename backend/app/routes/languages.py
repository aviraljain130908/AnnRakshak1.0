from fastapi import APIRouter
from app.schemas import LanguagesResponse

router = APIRouter(prefix="/languages", tags=["Languages"])

@router.get("", response_model=LanguagesResponse)
def get_supported_languages():
    """Returns the list of supported farmer interaction languages."""
    return {
        "languages": [
            {"code": "en", "name": "English"},
            {"code": "hi", "name": "Hindi"},
            {"code": "mr", "name": "Marathi"},
            {"code": "pa", "name": "Punjabi"},
            {"code": "ta", "name": "Tamil"},
            {"code": "te", "name": "Telugu"},
            {"code": "bn", "name": "Bengali"}
        ]
    }