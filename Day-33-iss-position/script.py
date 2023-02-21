import requests
from datetime import datetime

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_position = iss_response.json()

iss_lat = iss_position["iss_position"]["latitude"]
iss_lng = iss_position["iss_position"]["longitude"]

print(iss_lat)
print(iss_lng)

params = {
    "lat": 23.777176,
    "lng": 	90.399452,
    "formatted": 0
}

sun_info = requests.get(
    url=" https://api.sunrise-sunset.org/json", params=params)
sun_info.raise_for_status()

sun_data = sun_info.json()

sunrise = sun_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sun_data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
