from fastapi import APIRouter

router = APIRouter(prefix="/farmer", tags=["Farmer Advisory"])

@router.get("/info")
def get_farmer_system_info():
    """Simple system information endpoint for farmer applications."""
    return {
        "system": "Farmer Advisory & Disease Alert System",
        "supported_crops": ["Tomato", "Potato", "Rice", "Wheat"],
        "version": "1.0.0"
    }