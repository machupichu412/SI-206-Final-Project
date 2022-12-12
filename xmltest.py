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

def checkStatus(artistName):
        musicstorycid = "20c406eb9e965dafdfc7d97d08ff5f3a8f7756d4"
        musicstorysecret = "3c4aed05bd4ee3415fbd0bb449109a84ed2c20f9"
        token = "268bb5ff53b4f031c0e5ad70ae86f22948d91351"
        tokensecret = "ece7458d9440c3a337349d797abfbf9dd841d005"

        auth = OAuth1(musicstorycid, musicstorysecret, token, tokensecret)
        response = requests.get( "http://api.music-story.com/artist/search?", params = {'name': artistName}, auth = auth)
        print(response.text)
        tree = ET.fromstring(response.text)
        for i in range(len(tree[5])):
            if tree[5][i].find("type").text == "Person" and tree[5][i].find("name").text == artistName:
                    return True
            else:
                    return False

print(unidecode("Beyoncé"))
print(checkStatus(unidecode("Beyoncé")))