import requests
import os
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
owm_key = os.environ.get("OWM_API_KEY")
LAT = 51.160522
LNG = 71.470360

parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": owm_key,
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
