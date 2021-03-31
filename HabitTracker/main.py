import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "gizat"

user_params = {
    "token": "PRkpGkF8E66ib3hyTbQbBm483STGuy",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id"
}