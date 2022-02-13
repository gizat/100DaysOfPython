from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
billboard_100_webpage = response.text

soup = BeautifulSoup(billboard_100_webpage, "html.parser")

song_titles_soup = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_titles = [title.getText().strip() for title in song_titles_soup]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
                                               redirect_uri="https://example.com",
                                               scope="user-library-read playlist-modify-private"))

song_uris = []
year = date.split("-")[0]
for title in song_titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

user_id = sp.me()['id']
playlist = sp.user_playlist_create(user_id, f"{date} Billboard 100", public=False, collaborative=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
