import requests
import os
import smtplib
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("password")
email = os.getenv("email")

MY_LAT = 23.777176
MY_LONG = 90.399452


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_position = iss_response.json()

    iss_lat = iss_position["iss_position"]["latitude"]
    iss_lng = iss_position["iss_position"]["longitude"]

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_lng <= MY_LONG + 5:
        return True


def is_night():
    params = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    sun_info = requests.get(
        url=" https://api.sunrise-sunset.org/json", params=params)
    sun_info.raise_for_status()

    sun_data = sun_info.json()

    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time = datetime.now().hour

    if time < sunrise and time > sunset:
        return True


while True:
    time.sleep(60)
    print("Still running bro...")
    if is_night() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject: ISS Overhead\n\nLook up in the sky.")
