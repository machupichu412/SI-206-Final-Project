import xml.etree.ElementTree as ET
import json
from unidecode import unidecode
import requests
from requests_oauthlib import OAuth1
import sqlite3 as sql
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# checking if artist is individual or group using the Music Story API
def update_artist_table(artistName):
        api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(artistName)
        response = requests.get(api_url, headers={'X-Api-Key': 'QU/Mur5QkwH5le8q3vJXAw==ZePF0pHAnt3Lx2nO'})
        net_worth = 0
        age = 0
        if response.status_code == requests.codes.ok:
                js = json.loads(response.text)
                if(len(js) > 0):
                        for i in range(len(js)):
                                if js[i]["name"] == artistName.lower():
                                        net_worth = int(js[i].get("net_worth", -1))
                                        age = int(js[i].get("age", -1))
                                        return net_worth, age
                else:
                        return (-1, -1)
        else:
                print("Error:", response.status_code, response.text)
                return (-1, -1)
        return (-1, -1)

def checkStatus(artistName):
        musicstorycid = "20c406eb9e965dafdfc7d97d08ff5f3a8f7756d4"
        musicstorysecret = "3c4aed05bd4ee3415fbd0bb449109a84ed2c20f9"
        token = "268bb5ff53b4f031c0e5ad70ae86f22948d91351"
        tokensecret = "ece7458d9440c3a337349d797abfbf9dd841d005"

        auth = OAuth1(musicstorycid, musicstorysecret, token, tokensecret)
        response = requests.get( "http://api.music-story.com/artist/search?", params = {'name': artistName}, auth = auth)
        tree = ET.fromstring(response.text)
        for i in range(len(tree[5])):
            if tree[5][i].find("type").text == "Person" and tree[5][i].find("name").text == artistName:
                    return True
            else:
                    return False


def getArtists(genre, curr, conn):
        curr.execute("INSERT OR IGNORE INTO genre (genre_name) VALUES (?)", (genre.lower(), ))
        conn.commit()
        curr.execute("SELECT genre_id FROM genre WHERE genre_name = ?", (genre.lower(), ))
        genre_id = curr.fetchone()[0]
        conn.commit()
        count = 0
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
                        net_worth, age = update_artist_table(unidecode(name))
                        curr.execute("INSERT OR IGNORE INTO artists (name, net_worth, age) VALUES (?, ?, ?)", (name, net_worth, age))
                        conn.commit()
                        curr.execute("SELECT artist_id FROM artists WHERE name = ?", (name, ))
                        artist_id = curr.fetchone()[0]
                        conn.commit()
                        curr.execute("INSERT OR IGNORE INTO spotify (artist_id, popularity, genre_id) VALUES (?, ?, ?)", (artist_id, popularity, genre_id))
                        conn.commit()
                        count += 1
        print(f"added {count} artists to the database")

def main():
        conn = sql.connect("junkies.db")
        curr = conn.cursor()
        genre = input("Enter a genre: ")
        getArtists(genre, curr, conn)

main()

# 1	pop
# 2	hip-hop
# 3	indie
# 4	country
# 5	rock
# 6	edm
# 7	r&b
# 8	rap