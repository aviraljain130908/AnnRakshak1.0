from typing import Optional
from fastapi import APIRouter, Query
from app.schemas import WeatherResponse, WeatherRiskResponse
from app.services.weather_service import geocode_city, fetch_weather_data
from app.services.risk_prediction import calculate_weather_risk

router = APIRouter(prefix="/weather", tags=["Weather & Risk"])

@router.get("", response_model=WeatherResponse)
async def get_weather(
    latitude: Optional[float] = Query(None),
    longitude: Optional[float] = Query(None),
    location_name: Optional[str] = Query(None)
):
    """Retrieves current weather and 3-day forecast using Open-Meteo."""
    if latitude is None or longitude is None:
        city = location_name if location_name else "Jaipur"
        latitude, longitude = await geocode_city(city)

    weather_data = await fetch_weather_data(latitude, longitude)
    return weather_data

@router.get("/risk", response_model=WeatherRiskResponse)
async def get_weather_disease_risk(
    crop: str = Query(...),
    latitude: Optional[float] = Query(None),
    longitude: Optional[float] = Query(None),
    location_name: Optional[str] = Query(None)
):
    """Calculates weather-based disease and pest risks for a crop."""
    if latitude is None or longitude is None:
        city = location_name if location_name else "Jaipur"
        latitude, longitude = await geocode_city(city)

    weather_data = await fetch_weather_data(latitude, longitude)
    risk_result = calculate_weather_risk(
        crop, weather_data["current"], weather_data["forecast"]
    )

    return {
        "crop": crop,
        "weather": weather_data["current"],
        "risk": risk_result["primary"],
        "all_risks": risk_result["all_risks"]
    }