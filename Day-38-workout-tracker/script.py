import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')
app_id = os.getenv('app_id')

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": app_id,
    "x-app-key": api_key,
}

print(headers)

user_params = {
    "query": "ran 3 miles",
    "gender": "female",
    "weight_kg": 72.5,
    "height_cm": 167.64,
    "age": 30
}

res = requests.post(url=endpoint, json=user_params, headers=headers)
res.raise_for_status()
print(res.json())
