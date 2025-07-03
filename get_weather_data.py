import requests
import pandas as pd

import os

API_KEY = os.environ.get("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

cities = ["Tokyo", "Delhi", "Shanghai", "Mumbai", "Beijing", "Karachi", "Dhaka", "Seoul", "Jakarta", "Bangkok"]

weather_data = []
for city in cities:
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            "City": city,
            "Temperature (C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        })

df = pd.DataFrame(weather_data)
df.to_csv("asia_weather_data_2025.csv", index=False)

print("Weather data for Asian cities in 2025 has been downloaded and saved to asia_weather_data_2025.csv")
