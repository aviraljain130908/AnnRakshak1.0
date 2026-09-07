import httpx
from fastapi import HTTPException, status

async def geocode_city(city_name: str) -> tuple[float, float]:
    """Uses Open-Meteo's free Geocoding API to map city names to coordinates."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            resp = await client.get(url)
            data = resp.json()
            if "results" in data and len(data["results"]) > 0:
                result = data["results"][0]
                return float(result["latitude"]), float(result["longitude"])
            else:
                # Default fallback coordinates (Jaipur, India)
                return 26.9124, 75.7873
        except Exception:
            return 26.9124, 75.7873


async def fetch_weather_data(latitude: float, longitude: float) -> dict:
    """
    Fetches real current weather and 3-day forecast from Open-Meteo (no API key needed).
    Includes: temperature, humidity, rainfall, wind speed, precipitation probability, cloud cover.
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,rain,wind_speed_10m,cloud_cover"
        f"&daily=temperature_2m_max,temperature_2m_min,relative_humidity_2m_max,"
        f"relative_humidity_2m_min,rain_sum,precipitation_probability_max,"
        f"wind_speed_10m_max,cloud_cover_mean"
        f"&timezone=auto"
    )

    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(url)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=503,
                    detail={"success": False, "error": "Weather API unavailable"}
                )

            data = response.json()
            current_raw = data.get("current", {})
            daily_raw = data.get("daily", {})

            current = {
                "temperature": current_raw.get("temperature_2m", 28.0),
                "humidity": current_raw.get("relative_humidity_2m", 65.0),
                "rainfall": current_raw.get("rain", 0.0),
                "wind_speed": current_raw.get("wind_speed_10m", 10.0),
                "cloud_cover": current_raw.get("cloud_cover", 50.0)
            }

            forecast = []
            dates = daily_raw.get("time", [])
            temps_max = daily_raw.get("temperature_2m_max", [])
            temps_min = daily_raw.get("temperature_2m_min", [])
            hums_max = daily_raw.get("relative_humidity_2m_max", [])
            hums_min = daily_raw.get("relative_humidity_2m_min", [])
            rains = daily_raw.get("rain_sum", [])
            precip_probs = daily_raw.get("precipitation_probability_max", [])
            winds = daily_raw.get("wind_speed_10m_max", [])
            clouds = daily_raw.get("cloud_cover_mean", [])

            for i in range(min(3, len(dates))):
                forecast.append({
                    "date": dates[i],
                    "temperature": temps_max[i] if i < len(temps_max) else current["temperature"],
                    "temperature_min": temps_min[i] if i < len(temps_min) else current["temperature"],
                    "humidity": hums_max[i] if i < len(hums_max) else current["humidity"],
                    "humidity_min": hums_min[i] if i < len(hums_min) else current["humidity"],
                    "rainfall": rains[i] if i < len(rains) else 0.0,
                    "precipitation_probability": precip_probs[i] if i < len(precip_probs) else 0.0,
                    "wind_speed": winds[i] if i < len(winds) else current["wind_speed"],
                    "cloud_cover": clouds[i] if i < len(clouds) else current["cloud_cover"]
                })

            return {
                "location": {"latitude": latitude, "longitude": longitude},
                "current": current,
                "forecast": forecast
            }

        except HTTPException:
            raise
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail={"success": False, "error": "Weather information is currently unavailable"}
            )
