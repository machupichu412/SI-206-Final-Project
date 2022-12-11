import xml.etree.ElementTree as ET
import json
import requests
from requests_oauthlib import OAuth1
import xmltodict
import sqlite3 as sql
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# checking if artist is individual or group using the Music Story API
def checkStatus(artistName):
        musicstorycid = "20c406eb9e965dafdfc7d97d08ff5f3a8f7756d4"
        musicstorysecret = "3c4aed05bd4ee3415fbd0bb449109a84ed2c20f9"
        token = "268bb5ff53b4f031c0e5ad70ae86f22948d91351"
        tokensecret = "ece7458d9440c3a337349d797abfbf9dd841d005"

        auth = OAuth1(musicstorycid, musicstorysecret, token, tokensecret)
        response = requests.get( "http://api.music-story.com/artist/search?", params = {'name': artistName}, auth = auth)
        tree = ET.fromstring(response.text)
        if tree[5][0].find("type").text == "Person":
                return True
        else:
                return False


def getArtists(genre, curr, conn):
        curr.execute("INSERT OR IGNORE INTO genre (genre_name) VALUES (?)", (genre, ))
        conn.commit()
        curr.execute("SELECT genre_id FROM genre WHERE genre_name = ?", (genre, ))
        genre_id = curr.fetchone()[0]
        conn.commit()
        spotipycid = "f82a1ef57e2b4bab94afa5fc9f146d0f"
        spotipysecret = "bdb623d5ad514a5c9208d26b578479e9"
        client_credentials_manager = SpotifyClientCredentials(client_id=spotipycid, client_secret=spotipysecret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        artist_results = sp.search(q=f'genre:{genre}', type='artist', limit=25)
        artists = artist_results["artists"]["items"]
        for artist in artists:
                name = artist["name"]
                popularity = artist["popularity"]
                if checkStatus(name):
                        curr.execute("INSERT OR IGNORE INTO artists (name) VALUES (?)", (name, ))
                        conn.commit()
                        curr.execute("SELECT artist_id FROM artists WHERE name = ?", (name, ))
                        artist_id = curr.fetchone()[0]
                        conn.commit()
                        curr.execute("INSERT OR IGNORE INTO spotify (artist_id, popularity, genre_id) VALUES (?, ?, ?)", (artist_id, popularity, genre_id))
                        conn.commit()
        print("finished")

def main():
        conn = sql.connect("junkies.db")
        curr = conn.cursor()
        genre = input("Enter a genre: ")
        getArtists(genre, curr, conn)

main()