import requests
import json
import sqlite3 as sql
from unidecode import unidecode
from requests_oauthlib import OAuth1
import xml.etree.ElementTree as ET

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

def get_artist_from_tastedive(name, cur, conn):
    url = 'https://tastedive.com/api/similar'
    accesskey = "445402-SpotifyJ-NH86KIWN"

    param = {}

    param['q'] = name
    param['type'] = "music"
    param['limit'] = 25
    param['k'] = accesskey

    count = 0
    r = requests.get(url,params=param)
    js = json.loads(r.text)
    cur.execute("SELECT artist_id FROM artists WHERE name = ?", (name, ))
    primary_artist_id = cur.fetchone()[0]
    conn.commit()
    for items in js.values():
        results = items['Results']
        for i in results:
            artist_name = i['Name']
            if checkStatus(artist_name):
                count += 1
                net_worth, age = update_artist_table(unidecode(artist_name))
                cur.execute("INSERT OR IGNORE INTO artists (name, net_worth, age) VALUES (?, ?, ?)", (artist_name, net_worth, age))
                conn.commit()
                cur.execute("SELECT artist_id FROM artists WHERE name = ?", (artist_name, ))
                artist_id = cur.fetchone()[0]
                conn.commit()
                cur.execute("INSERT OR IGNORE INTO tastedive (artist_id, similar_artist_id) VALUES (?,?)", (primary_artist_id, artist_id))
                conn.commit()
    print(f"Added {count} artists to the database")
            
    
def main():
    conn = sql.connect("junkies.db")
    cur = conn.cursor()
    cur.execute("SELECT artists.name FROM artists")
    artists = [x[0] for x in cur.fetchall()]
    for artist in artists:
        print(artist)
    user_input = input("Enter an artist's name from the list: ")
    if user_input in artists:
        get_artist_from_tastedive(user_input, cur, conn)
    else:
        print("Sorry, that artist isn't in the database")

if __name__ == "__main__":
    main()
