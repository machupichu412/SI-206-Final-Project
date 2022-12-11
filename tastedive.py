import requests
import json
import sqlite3 as sql

accesskey = "445402-SpotifyJ-NH86KIWN"

def get_artist_from_tastedive(name, cur, conn):
    url = 'https://tastedive.com/api/similar'
    accesskey = "445402-SpotifyJ-NH86KIWN"

    param = {}

    param['q'] = name
    param['type'] = 'music'
    param['limit'] = 25
    param['k'] = accesskey

    r = requests.get(url,params=param)
    js = json.loads(r.text)
    for items in js.values():
        results = items['Results']
        for i in results:
            artist_name = i['Name']
            #cur.execute("SELECT artist_id FROM artists WHERE name = ?" (name, ))
            #inlist = cur.fetchall()
            #print(len(inlist))
            cur.execute("INSERT OR IGNORE INTO artists (name) VALUES (?)", (artist_name, ))
            conn.commit()
            cur.execute("SELECT artist_id FROM artists WHERE name = ?", (artist_name, ))
            artist_id = cur.fetchone()[0]
            conn.commit()
            art_type = i['Type']
            cur.execute("SELECT artist_id FROM artists WHERE name = ?", (name, ))
            primary_artist_id = cur.fetchone()[0]
            cur.execute("INSERT OR IGNORE INTO tastedive (artist_id, similar_artist_id, media_type) VALUES (?,?,?)", (primary_artist_id, artist_id, art_type))
            conn.commit()
            
    

def main():
    conn = sql.connect("junkies.db")
    cur = conn.cursor()
    print(get_artist_from_tastedive("Drake", cur, conn))

if __name__ == "__main__":
    main()
