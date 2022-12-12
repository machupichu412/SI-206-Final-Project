import xml.etree.ElementTree as ET
import json
import requests
from unidecode import unidecode
from requests_oauthlib import OAuth1
import sqlite3 as sql
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
str = """<?xml version="1.0" encoding="utf-8"?>\n<root><version>1.29</version><code>0</code><count>1</count><pageCount>1</pageCount><currentPage>1</currentPage><data><item><id>4579675</id><name>Post Malone</name><ipi/><type>Person</type><url>http://data.music-story.com/post-malone</url><firstname> Malone</firstname><lastname>Post</lastname><coeff_actu>16</coeff_actu><update_date>2022-06-23 09:07:04.107123</update_date><creation_date>2015-09-03 10:21:50</creation_date><search_scores><name>0</name></search_scores></item></data></root>"""

tree = ET.fromstring(str)
# print(tree[5][0].find("type").text)

# def checkStatus(artistName):
#         musicstorycid = "20c406eb9e965dafdfc7d97d08ff5f3a8f7756d4"
#         musicstorysecret = "3c4aed05bd4ee3415fbd0bb449109a84ed2c20f9"
#         token = "268bb5ff53b4f031c0e5ad70ae86f22948d91351"
#         tokensecret = "ece7458d9440c3a337349d797abfbf9dd841d005"

#         auth = OAuth1(musicstorycid, musicstorysecret, token, tokensecret)
#         response = requests.get( "http://api.music-story.com/artist/search?", params = {'name': artistName}, auth = auth)
#         print(response.text)
#         tree = ET.fromstring(response.text)
#         for i in range(len(tree[5])):
#             if tree[5][i].find("type").text == "Person" and tree[5][i].find("name").text == artistName:
#                     return True
#             else:
#                     return False

# print(unidecode("Beyoncé"))
# print(checkStatus(unidecode("Beyoncé")))


# def get_genre_list(cur, conn):
#     cur.execute("SELECT genre_name FROM genre")
#     genres = cur.fetchall()
#     genres = [x[0] for x in genres]
#     return genres

# def avg_networth_genre(genrename, cur, conn):
#     total = 0
#     count = 0

#     cur.execute("SELECT artists.net_worth FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 OR artists.net_worth != NULL AND genre.genre_name = ?", (genrename,))
#     networths = [x[0] for x in cur.fetchall()]
#     for networth in networths:
#         total += networth
#         count += 1
    
#     return networth/count

# def max_networth_genre(genrename, cur, conn):
#     cur.execute("SELECT artists.net_worth, artists.name FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 OR artists.net_worth != NULL AND genre.genre_name = ?", (genrename,))
#     networths = cur.fetchall()
#     print(networths)
#     maxnetworth = networths[0]
#     for networth in networths:
#         if networth[0] > maxnetworth[0]:
#             maxnetworth = networth
#     return maxnetworth

# def min_networth_genre(genrename, cur, conn):
#     cur.execute("SELECT artists.net_worth, artists.name FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 OR artists.net_worth != NULL AND genre.genre_name = ?", (genrename,))
#     networths = cur.fetchall()
#     minnetworth = networths[0]
#     for networth in networths:
#         if networth[0] < minnetworth[0]:
#             minnetworth = networth
#     return minnetworth

# def avg_net_worth_by_genre_vis(cur, conn):
#     genres = get_genre_list(cur, conn)
#     print(genres)
#     max_names = []
#     max_net_worths = []
#     min_names = []
#     min_net_worths = []
#     avg = []
#     for genre in genres:
#         max_net_worth, max_name = max_networth_genre(genre, cur, conn)
#         min_net_worth, min_name = min_networth_genre(genre, cur, conn)
#         avg_for_genre = avg_networth_genre(genre, cur, conn)
#         max_names.append(max_name)
#         max_net_worths.append(max_net_worth)
#         min_names.append(min_name)
#         min_net_worths.append(min_net_worth)
#         avg.append(avg_for_genre)
#     print(len(genres))
#     print(min_net_worths)

def max_networth_genre(genrename, cur, conn):
    cur.execute("SELECT artists.net_worth, artists.name FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 AND artists.net_worth IS NOT NULL AND genre.genre_name = ?", (genrename,))
    networths = cur.fetchall()
    maxnetworth = networths[0]
    for networth in networths:
        if networth[0] > maxnetworth[0]:
            maxnetworth = networth
    return maxnetworth

def min_networth_genre(genrename, cur, conn):
    cur.execute("SELECT artists.net_worth, artists.name FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 AND artists.net_worth IS NOT NULL AND genre.genre_name = ?", (genrename,))
    networths = cur.fetchall()
    minnetworth = networths[0]
    for networth in networths:
        if networth[0] < minnetworth[0]:
            minnetworth = networth
    return minnetworth

def avg_networth_genre(genrename, cur, conn):
    total = 0
    count = 0

    cur.execute("SELECT artists.net_worth FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 AND artists.net_worth IS NOT NULL AND genre.genre_name = ?", (genrename,))
    networths = [x[0] for x in cur.fetchall()]
    for networth in networths:
        total += networth
        print(networth)
        count += 1
        print(count)
    return total/count

conn = sql.connect("junkies.db")
cur = conn.cursor()
# avg_net_worth_by_genre_vis(cur, conn)
# print(max_networth_genre("r&b", cur, conn))

cur.execute("SELECT artists.net_worth FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 AND artists.net_worth IS NOT NULL AND genre.genre_name = ?", ("rock",))
print([x[0] for x in cur.fetchall()])

# print(max_networth_genre("rock", cur, conn))
# print(min_networth_genre("rock", cur, conn))
print(avg_networth_genre("rock", cur, conn))

