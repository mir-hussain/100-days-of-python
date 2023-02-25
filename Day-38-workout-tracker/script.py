import os
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')
app_id = os.getenv('app_id')
token = os.getenv('token')

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f03fc92c25e738c8d1b0bf6753b4d708/myWorkouts/workouts"

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

query = input("Enter your activity: ")

user_params = {
    "query": query,
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}


res = requests.post(url=endpoint, json=user_params, headers=headers)
res.raise_for_status()

activity_info = res.json()


workout_params = {
    "workout": {"date": dt.datetime.now().strftime("%x"),
                "time": dt.datetime.now().strftime("%X"),
                "exercise": activity_info["exercises"][0]["user_input"],
                "duration": activity_info["exercises"][0]["duration_min"],
                "calories": activity_info["exercises"][0]["nf_calories"]}
}

sheet_headers = {
    "Authorization": "Bearer " + token
}

sheet_res = requests.post(
    url=sheet_endpoint, json=workout_params, headers=sheet_headers)
sheet_res.raise_for_status()
print(sheet_res.json())
