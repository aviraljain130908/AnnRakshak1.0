# Crop Disease Detection & Farmer Advisory System Backend

A simple, beginner-friendly REST API backend for crop disease analysis, multilingual advisory, expert-support ticketing, and weather-based disease risk warnings.

## Features
1. **Multilingual Farmer Advisory**: Supported languages: English, Hindi, Marathi, Punjabi, Tamil, Telugu, and Bengali.
2. **Crop Image Analysis**: Automated file validation, blur detection (OpenCV), and plant health classification using open-source Hugging Face MobileNet models.
3. **Expert Support Tickets**: Farmers can post tickets with leaf photos. High-confidence disease detections auto-flag for urgent review.
4. **Weather & Pest Risk**: Open-Meteo Integration with rule-based pest risk calculations.

---

## Local Setup Instructions

### Prerequisites
- Python 3.9, 3.10, or 3.11 installed on your laptop.

### 1. Create and Activate Virtual Environment
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate