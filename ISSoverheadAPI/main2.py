import requests
import datetime

# Info for current place
MY_LAT = 42.333309
MY_LNG = 69.621811

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

print(datetime.now().hour)


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# lat = data["iss_position"]["latitude"]
# lon = data["iss_position"]["longitude"]

# iss_position = (lon, lat)

# print(iss_position)