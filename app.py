import streamlit as st
from utils.location import get_location_from_ip
from utils.aqi import get_aqi_by_coordinates, classify_aqi
from rag.retriever import retrieve_guideline
from rag.generator import generate_response



st.set_page_config(
    page_title="AirGuard AI",
    page_icon="🌍",
    layout="centered"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.title("🌍 AirGuard AI")
st.subheader("Breathe Better. Live Smarter.")
st.caption("AI-powered air quality & environmental health assistant")

st.markdown("---")

# --------------------------------------------------
# LOCATION SECTION
# --------------------------------------------------
from utils.location import get_location_from_ip, get_coordinates_from_city
from utils.aqi import get_aqi_by_coordinates, classify_aqi

location = get_location_from_ip()

use_manual = st.checkbox("✍️ Enter city manually")

if use_manual:
    city = st.text_input("Enter city name", placeholder="e.g., Delhi")

    if not city:
        st.warning("Please enter a city name.")
        st.stop()

    lat, lon = get_coordinates_from_city(city)

    if lat is None or lon is None:
        st.error("Unable to find coordinates for this city.")
        st.stop()

    st.success(f"📍 Selected Location: {city}")

else:
    city = location["city"]
    region = location["region"]
    country = location["country"]
    lat = location["lat"]
    lon = location["lon"]

    st.success(f"📍 Detected Location: {city}, {region}, {country}")

# --- AQI ---
aqi_value, pollutant = get_aqi_by_coordinates(lat, lon)
aqi_level, color = classify_aqi(aqi_value)

# --------------------------------------------------
# ENCOURAGING MESSAGE
# --------------------------------------------------
st.markdown(
    f"""
    <div style="
        padding:25px;
        border-radius:16px;
        background-color:{color};
        color:white;
        text-align:center;
        box-shadow:0px 6px 15px rgba(0,0,0,0.25);
    ">
        <h1 style="font-size:64px; margin-bottom:0;">{aqi_value}</h1>
        <h3 style="margin-top:5px;">AQI</h3>
        <p>Status: <b>{aqi_level}</b></p>
        <p>Dominant Pollutant: {pollutant}</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
st.markdown("## 🛡️ Safety & Health Measures (RAG-Based)")

retrieved_text = retrieve_guideline(aqi_value)
rag_output = generate_response(retrieved_text)

if rag_output:
    st.markdown("### 😷 Mask Recommendation")
    st.write(rag_output["mask"])

    st.markdown("### 🏠 Air Purifier")
    st.write(rag_output["purifier"])

    st.markdown("### 🏥 Health Check-up")
    st.write(rag_output["checkup"])

    st.markdown("### 📋 Step-by-Step Actions")
    for step in rag_output["actions"]:
        st.write(f"• {step}")

    st.success(rag_output["message"])
else:
    st.warning("Safety guidelines not available.")
