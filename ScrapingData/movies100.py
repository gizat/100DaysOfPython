from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2")
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

print(soup.prettify())
movies = soup.find_all(name="h3", class_="jsx-4245974604")
print(movies)