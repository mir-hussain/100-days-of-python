import os
import requests
from dotenv import load_dotenv

load_dotenv()

USERNAME = "mir-hussain"
TOKEN = os.getenv("token")

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

user_info = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# res = requests.post(url="https://pixe.la/v1/users", json=user_info)
# print(res.text)

graph_params = {
    "id": "graph1",
    "name": "Python Practice",
    "unit": "day",
    "type": "int",
    "color": "ajisai",
}

res = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(res.text)
