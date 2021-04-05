import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()  # take environment variables from .env.

class FlightSearch:
    
    def __init__(self):
        self.code = "TESTING"
        self.tequilla_api = os.environ.get("TEQUILLA_API")

    def get_destination_code(self, city_name):
        tequilla_ep = "https://tequila-api.kiwi.com/locations/query"
        
        headers = {
            "apikey":self.tequilla_api
        }
        params = {
            "term":city_name,
            "location_types": "city"
        }

        response = requests.get(url=tequilla_ep, params=params, headers=headers)
        result = response.json()["locations"]
        self.code = result[0]["code"]

        return self.code


    def search_flights(self, origin, destination, from_time, to_time):
        deals_ep = "https://tequila-api.kiwi.com/v2/search"

        headers = {
            "apikey":self.tequilla_api
        }

        query = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=deals_ep, params=query, headers=headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data