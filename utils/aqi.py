# utils/aqi.py
import requests

WAQI_TOKEN = "d161e7363188c5ce16d323528caf0a4bfbed706a"  

def get_aqi_by_coordinates(lat, lon):
    try:
        url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={WAQI_TOKEN}"
        response = requests.get(url)
        data = response.json()

        if data["status"] != "ok":
            return None, None

        aqi = data["data"]["aqi"]

        if aqi == "-" or aqi is None:
            return None, None

        pollutant = data["data"].get("dominentpol", "Unknown")
        return int(aqi), pollutant

    except Exception:
        return None, None


def classify_aqi(aqi):
    if aqi is None:
        return "Unknown", "#7f8c8d"

    if aqi <= 50:
        return "Good", "#2ecc71"
    elif aqi <= 100:
        return "Moderate", "#f1c40f"
    elif aqi <= 200:
        return "Poor", "#e67e22"
    elif aqi <= 300:
        return "Very Poor", "#e74c3c"
    else:
        return "Severe", "#8e44ad"