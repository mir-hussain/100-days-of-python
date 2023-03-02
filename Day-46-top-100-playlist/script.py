import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint

pp = pprint.PrettyPrinter(depth=4)

load_dotenv()

client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
redirect_uri = "http://example.com"
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

user_id = sp.current_user()["id"]

date = input("Enter the year you wanna travel to in this format YYYY-MM-DD ")
year = date.split("-")[0]


res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

titles = soup.select("li ul li h3")

title_list = [title.get_text(strip=True) for title in titles]


song_uris = []

for title in title_list:

    result = sp.search(q=f"track:{title} year:{year}", type="track")

    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{title} Doesn't Exist on Spotify. Skipped")

sp.playlist()
