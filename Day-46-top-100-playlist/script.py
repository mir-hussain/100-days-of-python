import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = "http://example.com"


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])

# date = input("Enter the year you wanna travel to in this format YYYY-MM-DD ")


# res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "html.parser")

# titles = soup.select("li ul li h3")

# title_list = [title.get_text(strip=True) for title in titles]

# print(title_list)
