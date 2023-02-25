import os
from dotenv import load_dotenv

load_dotenv()

app_key = os.getenv('app_key')
app_id = os.getenv('app_id')

headers = {
    "x-app-id": app_id,
    "x-app-key": app_key,
    "Content-Type": "application/json"
}
