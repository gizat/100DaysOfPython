import requests
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

class DataManager:
    
    def __init__(self):
        self.sheety_auth = os.environ.get("SHEETY_AUTH")
        self.sheety_ep = os.environ.get("SHEETY_ENDPOINT")
        self.destination_data = {}
    

    def get_destination_data(self):
        sheety_header = {
            "Authorization": self.sheety_auth,
            "Content-Type": "application/json"
        }

        sheety_response = requests.get(url=self.sheety_ep, headers=sheety_header)
        self.destination_data = sheety_response.json()["prices"]
        return self.destination_data


    def update_destination_codes(self):
        sheety_header = {
            "Authorization": self.sheety_auth,
            "Content-Type": "application/json"
        }

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            endpoint = f"{self.sheety_ep}/{city['id']}"

            response = requests.put(url=endpoint, headers=sheety_header, json=new_data)
