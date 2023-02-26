from bs4 import BeautifulSoup
import requests


imdb = requests.get(
    "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")

soup = BeautifulSoup(imdb.text, "html.parser")

movies = soup.select(".lister-item-header a")


with open("movie_list.txt", "w") as file:
    movies_list = [
        f"{movie[0] + 1}. {movie[1].text} https://www.imdb.com/{movie[1].get('href')}" for movie in enumerate(movies)]

    for movie in movies_list:
        file.write(f"{movie}\n")
