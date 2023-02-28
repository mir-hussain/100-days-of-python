from bs4 import BeautifulSoup
import requests

date = input("Enter the year you wanna travel to in this format YYYY-MM-DD ")


res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")
print(soup.prettify())
