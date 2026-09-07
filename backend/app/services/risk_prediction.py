"""
Crop-specific weather-based disease and pest risk prediction.
Uses multi-factor scoring (humidity, temperature, rainfall, wind, precipitation probability)
with per-crop disease vulnerability profiles.
"""

# Disease vulnerability profiles per crop.
# Each entry: {disease_name: {conditions}}
# Conditions drive the risk scoring logic in calculate_weather_risk().
CROP_PROFILES = {
    "tomato": {
        "diseases": {
            "Late Blight (Phytophthora infestans)": {
                "humidity_min": 70, "temp_min": 10, "temp_max": 25, "rain_threshold": 2.0,
                "severity": "critical"
            },
            "Early Blight (Alternaria solani)": {
                "humidity_min": 60, "temp_min": 24, "temp_max": 30, "rain_threshold": 0,
                "severity": "moderate"
            },
            "Septoria Leaf Spot": {
                "humidity_min": 65, "temp_min": 20, "temp_max": 28, "rain_threshold": 1.0,
                "severity": "moderate"
            },
            "Leaf Mold": {
                "humidity_min": 85, "temp_min": 22, "temp_max": 26, "rain_threshold": 0,
                "severity": "moderate"
            },
            "Bacterial Spot": {
                "humidity_min": 65, "temp_min": 24, "temp_max": 32, "rain_threshold": 1.0,
                "wind_min": 15, "severity": "moderate"
            },
            "Whitefly / TYLCV Vector": {
                "humidity_min": 40, "temp_min": 28, "temp_max": 40, "rain_threshold": -1,
                "severity": "moderate", "pest": True
            }
        },
        "recommendations": {
            "fungal": [
                "Apply Mancozeb 75% WP @ 2.5 g/L preventively",
                "Avoid overhead irrigation — use drip irrigation",
                "Stake and prune plants for better air circulation",
                "Monitor daily for lesion appearance on lower leaves"
            ],
            "pest": [
                "Install yellow sticky traps to monitor whitefly levels",
                "Spray Imidacloprid 17.8% SL @ 0.5 mL/L for whitefly control",
                "Use reflective mulches to repel whiteflies",
                "Inspect undersides of leaves for spider mites and aphids"
            ],
            "general": [
                "Ensure good drainage to avoid waterlogging",
                "Remove and destroy infected plant debris"
            ]
        }
    },

    "potato": {
        "diseases": {
            "Late Blight (Phytophthora infestans)": {
                "humidity_min": 70, "temp_min": 10, "temp_max": 24, "rain_threshold": 2.0,
                "severity": "critical"
            },
            "Early Blight (Alternaria solani)": {
                "humidity_min": 60, "temp_min": 24, "temp_max": 29, "rain_threshold": 0,
                "severity": "moderate"
            },
            "Black Scurf (Rhizoctonia solani)": {
                "humidity_min": 75, "temp_min": 10, "temp_max": 18, "rain_threshold": 1.0,
                "severity": "low"
            }
        },
        "recommendations": {
            "fungal": [
                "Apply Metalaxyl 8% + Mancozeb 64% WP @ 2.5 g/L at first symptom",
                "Hill up soil around plants to protect tubers",
                "Destroy infected haulm (stems) before harvest",
                "Monitor daily — Late Blight can destroy crop in 3–5 days under wet conditions"
            ],
            "pest": [
                "Scout for aphids — they transmit virus diseases",
                "Spray Imidacloprid or Thiamethoxam for aphid control",
                "Check for Colorado potato beetle egg masses on leaf undersides"
            ],
            "general": [
                "Use certified disease-free seed tubers",
                "Rotate crops — avoid planting potato after tomato or pepper"
            ]
        }
    },

    "rice": {
        "diseases": {
            "Rice Blast (Magnaporthe oryzae)": {
                "humidity_min": 80, "temp_min": 24, "temp_max": 30, "rain_threshold": 3.0,
                "severity": "critical"
            },
            "Bacterial Leaf Blight (Xanthomonas oryzae)": {
                "humidity_min": 75, "temp_min": 25, "temp_max": 35, "rain_threshold": 1.0,
                "wind_min": 20, "severity": "critical"
            },
            "Sheath Blight (Rhizoctonia solani)": {
                "humidity_min": 85, "temp_min": 28, "temp_max": 32, "rain_threshold": 0,
                "severity": "moderate"
            },
            "Brown Planthopper": {
                "humidity_min": 75, "temp_min": 26, "temp_max": 32, "rain_threshold": 0,
                "severity": "critical", "pest": True
            }
        },
        "recommendations": {
            "fungal": [
                "Apply Tricyclazole 75% WP @ 0.6 g/L for blast control",
                "Drain fields for 3–5 days to reduce Sheath Blight",
                "Avoid excess nitrogen — it increases blast susceptibility",
                "Monitor panicle necks for blast at heading stage"
            ],
            "pest": [
                "Monitor for brown planthopper using light traps",
                "Spray Buprofezin 25% SC @ 1 mL/L for planthopper control",
                "Drain field temporarily to expose pests",
                "Avoid excessive urea application — it attracts planthoppers"
            ],
            "general": [
                "Maintain 2–3 cm standing water during critical growth stages",
                "Use resistant varieties (e.g., IR64, Swarna Sub1)"
            ]
        }
    },

    "wheat": {
        "diseases": {
            "Yellow Rust / Stripe Rust (Puccinia striiformis)": {
                "humidity_min": 60, "temp_min": 10, "temp_max": 15, "rain_threshold": 0,
                "severity": "critical"
            },
            "Brown Rust / Leaf Rust (Puccinia triticina)": {
                "humidity_min": 60, "temp_min": 15, "temp_max": 25, "rain_threshold": 0,
                "severity": "critical"
            },
            "Powdery Mildew (Blumeria graminis)": {
                "humidity_min": 70, "temp_min": 15, "temp_max": 22, "rain_threshold": 0,
                "severity": "moderate"
            },
            "Loose Smut (Ustilago tritici)": {
                "humidity_min": 65, "temp_min": 16, "temp_max": 22, "rain_threshold": 1.0,
                "severity": "moderate"
            }
        },
        "recommendations": {
            "fungal": [
                "Apply Propiconazole 25% EC @ 1 mL/L at flag leaf stage for rust",
                "Use Tebuconazole 25.9% EC @ 1 mL/L for severe rust infections",
                "Scout fields regularly — rust can spread rapidly in cool, humid conditions",
                "Apply fungicide before heading stage for best results"
            ],
            "pest": [
                "Monitor for aphids on ears — they transmit Barley Yellow Dwarf Virus",
                "Spray Dimethoate 30% EC @ 1.5 mL/L for aphid control",
                "Check for termite activity near field borders"
            ],
            "general": [
                "Use rust-resistant varieties (e.g., HD2967, PBW550)",
                "Avoid late sowing — early-sown wheat is less vulnerable to rust"
            ]
        }
    },

    "maize": {
        "diseases": {
            "Gray Leaf Spot / Cercospora (Cercospora zeae-maydis)": {
                "humidity_min": 70, "temp_min": 22, "temp_max": 30, "rain_threshold": 1.0,
                "severity": "moderate"
            },
            "Northern Leaf Blight (Exserohilum turcicum)": {
                "humidity_min": 65, "temp_min": 18, "temp_max": 27, "rain_threshold": 1.0,
                "severity": "moderate"
            },
            "Common Rust (Puccinia sorghi)": {
                "humidity_min": 60, "temp_min": 16, "temp_max": 23, "rain_threshold": 0,
                "severity": "moderate"
            },
            "Fall Armyworm (Spodoptera frugiperda)": {
                "humidity_min": 50, "temp_min": 25, "temp_max": 35, "rain_threshold": 0,
                "severity": "critical", "pest": True
            }
        },
        "recommendations": {
            "fungal": [
                "Apply Azoxystrobin 23% SC @ 1 mL/L at tasseling for fungal control",
                "Use Propiconazole 25% EC @ 1 mL/L for rust",
                "Scout lower canopy leaves — Gray Leaf Spot starts from bottom",
                "Rotate with non-host crops (soybean, groundnut)"
            ],
            "pest": [
                "Check whorl leaves for Fall Armyworm feeding damage (window-pane effect)",
                "Apply Chlorpyrifos 50% EC @ 2 mL/L or Spinosad 45% SC @ 0.3 mL/L",
                "Use pheromone traps to monitor Fall Armyworm adult populations",
                "Apply Bt (Bacillus thuringiensis) for early instar larvae"
            ],
            "general": [
                "Use hybrid varieties with partial resistance to Turcicum blight",
                "Destroy crop residue post-harvest to reduce inoculum load"
            ]
        }
    }
}

# Generic profile used when crop is not in CROP_PROFILES
GENERIC_PROFILE = {
    "recommendations": {
        "fungal": [
            "Apply broad-spectrum fungicide (Mancozeb 75% WP @ 2.5 g/L)",
            "Improve air circulation around plants",
            "Avoid overhead irrigation during humid periods"
        ],
        "pest": [
            "Scout for aphids, whiteflies, and mites regularly",
            "Apply Imidacloprid or Neem-based insecticide if pest populations are high"
        ],
        "general": [
            "Monitor crops daily during high-risk weather periods",
            "Remove and destroy diseased plant material"
        ]
    }
}


def _score_disease_risk(disease_name: str, profile: dict, current: dict, forecast: list) -> float:
    """
    Scores a disease risk from 0–100 based on current + forecast weather conditions.
    Returns a float risk score.
    """
    temp = current.get("temperature", 25.0)
    humidity = current.get("humidity", 50.0)
    rainfall = current.get("rainfall", 0.0)
    wind_speed = current.get("wind_speed", 10.0)

    # Forecast analysis: max humidity and total rain across 3 days
    forecast_humidity_max = max((d.get("humidity", 0) for d in forecast), default=humidity)
    forecast_rain_sum = sum(d.get("rainfall", 0) for d in forecast)
    forecast_precip_prob_max = max((d.get("precipitation_probability", 0) for d in forecast), default=0)

    effective_humidity = max(humidity, forecast_humidity_max * 0.7)
    effective_rain = max(rainfall, forecast_rain_sum / max(len(forecast), 1))

    score = 0.0

    # Humidity score (0–40 points)
    h_min = profile.get("humidity_min", 60)
    if effective_humidity >= h_min:
        humidity_excess = min((effective_humidity - h_min) / (100 - h_min), 1.0)
        score += 40.0 * humidity_excess

    # Temperature score (0–25 points) — checks if temp is in the disease-favorable range
    t_min = profile.get("temp_min", 10)
    t_max = profile.get("temp_max", 40)
    if t_min <= temp <= t_max:
        temp_center = (t_min + t_max) / 2
        temp_fit = 1.0 - abs(temp - temp_center) / max((t_max - t_min) / 2, 1)
        score += 25.0 * temp_fit

    # Rainfall / wetness score (0–25 points)
    rain_threshold = profile.get("rain_threshold", 0)
    if rain_threshold >= 0:  # -1 means dry conditions favor this disease
        if effective_rain > rain_threshold or forecast_precip_prob_max >= 50:
            rain_factor = min(effective_rain / max(rain_threshold + 2, 2), 1.0)
            precip_prob_factor = forecast_precip_prob_max / 100.0
            score += 25.0 * max(rain_factor, precip_prob_factor)
    else:
        # Disease favored by dry conditions (e.g., whitefly)
        if effective_rain < 1.0:
            score += 20.0

    # Wind score (0–10 points) — high wind helps spread bacterial/spore diseases
    wind_min = profile.get("wind_min", 0)
    if wind_min > 0 and wind_speed >= wind_min:
        score += 10.0

    return min(score, 100.0)


def _score_to_level(score: float) -> str:
    if score >= 60:
        return "High Risk"
    elif score >= 35:
        return "Medium Risk"
    else:
        return "Low Risk"


def calculate_weather_risk(crop: str, current_weather: dict, forecast: list) -> dict:
    """
    Calculates crop-specific weather-based disease and pest risks.
    Returns the highest-priority risk as primary + all evaluated risks.
    """
    crop_lower = crop.lower().strip()
    profile = CROP_PROFILES.get(crop_lower, None)
    recommendations_pool = (profile or GENERIC_PROFILE)["recommendations"]

    if profile is None:
        # Fallback to generic 3-rule logic for unknown crops
        return _generic_risk_fallback(crop, current_weather, forecast, recommendations_pool)

    evaluated_risks = []

    for disease_name, disease_profile in profile["diseases"].items():
        score = _score_disease_risk(disease_name, disease_profile, current_weather, forecast)
        level = _score_to_level(score)
        is_pest = disease_profile.get("pest", False)
        severity = disease_profile.get("severity", "moderate")

        # Build reason
        temp = current_weather.get("temperature", 25.0)
        humidity = current_weather.get("humidity", 50.0)
        forecast_rain = sum(d.get("rainfall", 0) for d in forecast)
        reason = (
            f"Temperature {temp}°C, humidity {humidity}%, "
            f"forecast rainfall {round(forecast_rain, 1)} mm — "
            f"{'favorable' if score >= 35 else 'not ideal'} conditions for {disease_name}."
        )

        rec_key = "pest" if is_pest else "fungal"
        recs = recommendations_pool.get(rec_key, []) + recommendations_pool.get("general", [])

        evaluated_risks.append({
            "disease": disease_name,
            "level": level,
            "score": round(score, 1),
            "severity": severity,
            "is_pest": is_pest,
            "reason": reason,
            "recommendations": recs[:4]  # top 4 recommendations
        })

    # Sort by score descending
    evaluated_risks.sort(key=lambda x: x["score"], reverse=True)

    # Build response list
    all_risks = []
    for r in evaluated_risks:
        all_risks.append({
            "level": r["level"],
            "reason": r["reason"],
            "alert": f"{r['level']} of {r['disease']} on {crop}.",
            "threats": [r["disease"]],
            "recommendations": r["recommendations"]
        })

    # Primary = highest scoring risk
    primary = all_risks[0] if all_risks else {
        "level": "Low Risk",
        "reason": "No significant risk factors detected.",
        "alert": "Current weather is within safe limits for crop health.",
        "threats": [],
        "recommendations": recommendations_pool.get("general", [])
    }

    # Also expose all_risks (filter out Low Risk entries for cleaner output, keep at least one)
    notable_risks = [r for r in all_risks if r["level"] != "Low Risk"]
    if not notable_risks:
        notable_risks = [all_risks[0]] if all_risks else [primary]

    return {
        "primary": primary,
        "all_risks": notable_risks
    }


def _generic_risk_fallback(crop: str, current: dict, forecast: list, recommendations: dict) -> dict:
    """Fallback logic for crops not in CROP_PROFILES."""
    temp = current.get("temperature", 25.0)
    humidity = current.get("humidity", 50.0)
    rainfall = current.get("rainfall", 0.0)
    upcoming_rain = sum(d.get("rainfall", 0) for d in forecast)

    if humidity >= 75.0 and (rainfall > 2.0 or upcoming_rain > 5.0):
        level = "High Risk"
        reason = f"High humidity ({humidity}%) combined with wet weather creates ideal conditions for fungal spread on {crop}."
        alert = f"High risk of fungal diseases (Blight / Mildew) on {crop} over the next 3 days."
        threats = ["Fungal Blight", "Downy Mildew"]
        recs = recommendations.get("fungal", []) + recommendations.get("general", [])
    elif 25.0 <= temp <= 35.0 and 60.0 <= humidity < 75.0:
        level = "Medium Risk"
        reason = f"Warm temperatures ({temp}°C) and moderate humidity ({humidity}%) may encourage pest activity."
        alert = f"Moderate risk of aphid and pest activity on {crop}."
        threats = ["Aphids", "Whitefly"]
        recs = recommendations.get("pest", []) + recommendations.get("general", [])
    else:
        level = "Low Risk"
        reason = "Current weather conditions are within normal ranges for standard crop health."
        alert = "Low disease risk under current weather patterns."
        threats = []
        recs = recommendations.get("general", [])

    risk = {
        "level": level,
        "reason": reason,
        "alert": alert,
        "threats": threats,
        "recommendations": recs[:4]
    }
    return {"primary": risk, "all_risks": [risk]}
