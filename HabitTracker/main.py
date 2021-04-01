import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()  # take environment variables from .env.

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "gizat"
TOKEN = os.environ.get("PIXELA_TOKEN")

headers = {
    "X-USER-TOKEN": TOKEN
}

### ADD A PIXEL

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

today = datetime.datetime.now().strftime("%Y%m%d")
quantity = 4

pixel_params = {
    "date": str(today),
    "quantity": str(quantity)
}

response = requests.post(url=graph_endpoint, headers=headers, json=pixel_params)
print(response.text)


### CREATE A GRAPH 

# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "pomodoro",
#     "type": "int",
#     "color": "shibafu"
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


### CREATE A USER

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }