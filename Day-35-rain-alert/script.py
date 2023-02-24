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
weather_req.raise_for_status()

weather_data = weather_req.json()
hour_list = weather_data["hourly"][:12]


def check_for_rain():
    rain: bool
    for hour_info in hour_list:
        if hour_info["weather"][0]["main"] == "Rain":
            rain = True
            break
        else:
            rain = False

    return rain


print(check_for_rain())


# print(weather_data["hourly"][0]["weather"][0]["main"])
