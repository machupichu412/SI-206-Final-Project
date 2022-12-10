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


def getArtists(sp):
        count = 0
        artist_results = sp.search(q='genre:pop', type='artist', limit=25)
        # for i in artist_results:
        #         count += 1
        print(artist_results)
