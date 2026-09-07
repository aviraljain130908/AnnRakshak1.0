import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.database import Base, engine
from app.services.disease_model import disease_model_instance
from app.routes import languages, disease, tickets, weather, farmer

# Startup & Shutdown lifecycle handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Auto-create SQLite database tables on startup
    Base.metadata.create_all(bind=engine)
    
    # Load AI model into CPU memory at startup
    disease_model_instance.load()
    yield

app = FastAPI(
    title="Crop Disease Detection & Farmer Advisory API",
    description="A beginner-friendly REST API for crop health, expert support, and weather advisory.",
    version="1.0.0",
    lifespan=lifespan
)

# Read CORS origins from environment variable
origins_env = os.getenv("ALLOWED_CORS_ORIGINS", "http://localhost:3000,http://localhost:5173")
origins = [origin.strip() for origin in origins_env.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve uploaded images statically
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Mount Route Handlers
app.include_router(languages.router)
app.include_router(disease.router)
app.include_router(tickets.router)
app.include_router(weather.router)
app.include_router(farmer.router)

@app.get("/health", tags=["Health Check"])
def health_check():
    """Health check endpoint confirming the backend server is operational."""
    return {"status": "ok"}