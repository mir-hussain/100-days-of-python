import requests
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

MY_LAT = 23.777176
MY_LONG = 90.399452
EMAIL = os.getenv("email")
PASSWORD = os.getenv("password")
MAIL = ''
print(EMAIL)
print(PASSWORD)

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


if check_for_rain():
    MAIL = "It's going to rain today. Take your umbrella"
else:
    MAIL = "Chill, no rain in next 12 hours"


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL,
                     password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=EMAIL,
        msg=f"Subject: Rain alert\n\n{MAIL}"
    )
    print(f"Mail send {MAIL}")
