import requests
import sqlite3 as sql

def get_artist_info(cur, conn):
    cur.execute ("SELECT name FROM artists")
    artist_list = cur.fetchall()
    artists = [x[0] for x in artist_list]
    return artists

def update_artist_table(artists, cur, conn):
    for i in artists:
        name = i
        api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': 'QU/Mur5QkwH5le8q3vJXAw==ZePF0pHAnt3Lx2nO'})
        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:", response.status_code, response.text)