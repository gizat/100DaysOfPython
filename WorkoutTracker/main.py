import requests
import os
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.

GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 183
AGE = 33

APP_ID = os.environ.get("NUTRITIONIX_ID")
API_KEY = os.environ.get("NUTRITIONIX_KEY")

nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutri_endpoint, headers=headers, json=exercise_params)
result = response.json()
print(result)


### SHEETY

sheety_endpoint = "https://api.sheety.co/9e7c3955c1f93c0cc16948155a0b3f9e/myWorkouts/workouts"

