import pprint
import sys
import sqlite3 as sql
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

scope = "user-library-read"
cid = "f82a1ef57e2b4bab94afa5fc9f146d0f"
secret = "bdb623d5ad514a5c9208d26b578479e9"


client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


artist_name = []
track_name = []
popularity = []
track_id = []
track_results = sp.search(q='year:2018', type='track', limit=25)
for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

print(len(artist_name))