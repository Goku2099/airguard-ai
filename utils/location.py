# utils/location.py
import requests
from geopy.geocoders import Nominatim

def get_location_from_ip():
    response = requests.get("https://ipapi.co/json/")
    data = response.json()
    return {
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country_name"),
        "lat": data.get("latitude"),
        "lon": data.get("longitude"),
    }

def get_coordinates_from_city(city):
    geolocator = Nominatim(user_agent="airguard-ai")
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    return None, None
