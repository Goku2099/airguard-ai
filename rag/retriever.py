def retrieve_guideline(aqi):
    with open("data/guidelines.txt", "r") as f:
        text = f.read()

    sections = text.split("\n\n")

    for section in sections:
        if "[AQI:0-50]" in section and aqi <= 50:
            return section
        elif "[AQI:51-100]" in section and 51 <= aqi <= 100:
            return section
        elif "[AQI:101-200]" in section and 101 <= aqi <= 200:
            return section
        elif "[AQI:201-300]" in section and 201 <= aqi <= 300:
            return section
        elif "[AQI:301+]" in section and aqi >= 301:
            return section

    return None
