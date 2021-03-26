import requests
from datetime import datetime
import time

MY_LAT = 42.333309
MY_LNG = 69.621811

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(iss_latitude - MY_LAT) < 5 or abs(iss_longitude - MY_LNG) < 5:
        return True
    else:
        return False


def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 6
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 6

    time_now = datetime.now()
    
    if time_now.hour <= sunrise and time_now.hour >= sunset:
        return True
    else:
        return False


while True:
    if is_dark() and is_iss_overhead():
        print("Look up!")
    else:
        print("Not yet.")

    time.sleep(60)