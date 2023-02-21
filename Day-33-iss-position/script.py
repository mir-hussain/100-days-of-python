import requests

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_position = iss_response.json()

iss_lat = iss_position["iss_position"]["latitude"]
iss_long = iss_position["iss_position"]["longitude"]

print(iss_lat)
print(iss_long)
