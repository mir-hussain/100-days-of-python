import requests
import os
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 23.777176
MY_LONG = 90.399452

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("key")

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key
}

weather_req = requests.get(url=endpoint, params=params)

weather_data = weather_req.json()
print(weather_data)
