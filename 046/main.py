from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from os import getenv
from pprint import pprint

load_dotenv()
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

# scraping from Billboard 100
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:"
)

year = date.split("-")[0]

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")

songs = soup.select(selector="li ul li h3")
songs_list = [song.getText().strip() for song in songs]
song_names = [title for title in songs_list]

# authenticating Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="046/token.txt",
    )
)
user_id = sp.current_user()["id"]


# getting uris of the songs from the list
song_uris = []
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} not found in Spotify.")

# creating playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    collaborative=None,
)
playlist_id = playlist["id"]

# adding songs to the playlist
sp.user_playlist_add_tracks(
    user=user_id,
    playlist_id=playlist_id,
    tracks=song_uris,
)
