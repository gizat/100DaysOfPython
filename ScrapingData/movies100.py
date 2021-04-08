from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512")
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

all_movies = soup.find_all(name="h1", class_="list-item__title")
movies = [movie.getText() for movie in all_movies]
movie_titles = movies[::-1]

with open('movies.txt', mode='w') as file:
    for i in range(len(movie_titles)):
        contents = file.write(f"{i+1}) {movie_titles[i]}\n")