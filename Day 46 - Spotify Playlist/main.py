from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = "68889e25a76a4eb7ac880601a2a56599"
CLIENT_SECRET = "92974480d1a54c80a9f0b929ab527d32"
REDIRECT_URI = "https://example.com/callback"
SCOPE = "playlist-modify-private"


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all(name="h3", class_="u-letter-spacing-0021", id="title-of-a-story")
top_100_songs_names = [song.text.strip() for song in song_names_spans]
top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Songwriter(s):')
top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Producer(s):')
top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Imprint/Promotion Label:')

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SCOPE,
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path=None
    )
)
user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in top_100_songs_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
