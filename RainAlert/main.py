import requests
from datetime import datetime
import time

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "5f13e15835bca2f8334712f94a3be14f"
# LAT = 51.160522
# LNG = 71.470360

LAT = 54.619570
LNG = 25.244190

parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

forecast_data = weather_data["hourly"][0:12]

for hour in forecast_data:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella.")
        break
