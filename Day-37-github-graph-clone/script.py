import os
import datetime as dt
import requests
from dotenv import load_dotenv

load_dotenv()

USERNAME = "mir-hussain"
TOKEN = os.getenv("token")


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

user_info = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


def formatted_date():
    date = dt.datetime.now()
    year = date.year
    month = date.month
    day = date.day

    if month < 10:
        month = f"0{month}"

    if day < 10:
        day = f"0{day}"

    return f"{year}{month}{day}"

# res = requests.post(url="https://pixe.la/v1/users", json=user_info)
# print(res.text)

# graph_params = {
#     "id": "graph1",
#     "name": "Python Practice",
#     "unit": "day",
#     "type": "int",
#     "color": "ajisai",
# }

# res = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(res.text)


# pixel_params = {
#     "date": formatted_date(),
#     "quantity": "1"
# }

# res = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

# print(res.text)
