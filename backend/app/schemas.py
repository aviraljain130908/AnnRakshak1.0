from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

# --- Language Schemas ---
class Language(BaseModel):
    code: str
    name: str

class LanguagesResponse(BaseModel):
    languages: List[Language]

# --- Disease Detection Schemas ---
class AlternativePrediction(BaseModel):
    label: str
    confidence: float

class DiseaseDetectionResponse(BaseModel):
    id: int
    crop: str
    result: str
    confidence: float
    status: str
    message: str
    basic_advice: str
    treatment: Optional[str] = None
    language: str
    image_path: str
    alternatives: List[AlternativePrediction] = []

    model_config = ConfigDict(from_attributes=True)

# --- Ticket System Schemas ---
class TicketCreate(BaseModel):
    crop_type: str
    location: str
    problem_description: str
    language: Optional[str] = "en"

class TicketUpdate(BaseModel):
    status: Optional[str] = None
    expert_response: Optional[str] = None

class TicketResponse(BaseModel):
    id: int
    crop_type: str
    image_path: str
    location: str
    problem_description: str
    language: str
    ai_result: Optional[str] = None
    ai_confidence: Optional[float] = None
    status: str
    expert_response: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

# --- Weather & Risk Schemas ---
class CurrentWeather(BaseModel):
    temperature: float
    humidity: float
    rainfall: float
    wind_speed: float
    cloud_cover: Optional[float] = None

class WeatherForecastItem(BaseModel):
    date: str
    temperature: float
    temperature_min: Optional[float] = None
    humidity: float
    humidity_min: Optional[float] = None
    rainfall: float
    precipitation_probability: Optional[float] = None
    wind_speed: float
    cloud_cover: Optional[float] = None

class WeatherResponse(BaseModel):
    location: dict
    current: CurrentWeather
    forecast: List[WeatherForecastItem]

class RiskInfo(BaseModel):
    level: str  # Low Risk, Medium Risk, High Risk
    reason: str
    alert: str
    threats: List[str] = []
    recommendations: List[str] = []

class WeatherRiskResponse(BaseModel):
    crop: str
    weather: CurrentWeather
    risk: RiskInfo
    all_risks: List[RiskInfo] = []