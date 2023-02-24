import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")

user_info = {
    "token": token,
    "username": "mir-hussain",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# res = requests.post(url="https://pixe.la/v1/users", json=user_info)
# print(res.text)
