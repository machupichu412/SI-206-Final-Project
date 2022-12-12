import requests
import sqlite3 as sql
import json


def get_artist_names(cur, conn):
    cur.execute("SELECT name FROM artists")
    artist_list = cur.fetchall()
    artists = [x[0] for x in artist_list]
    return artists

def update_artist_table(artists, cur, conn):
    for i in artists:
        name = i
        api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': 'QU/Mur5QkwH5le8q3vJXAw==ZePF0pHAnt3Lx2nO'})
        if response.status_code == requests.codes.ok:
            js = json.loads(response.text)
            if(len(js) > 0):
                for i in range(len(js)):
                    if js[i]["name"] == name.lower():
                        net_worth = int(js[i].get("net_worth", -1))
                        age = int(js[i].get("age", -1))
                        cur.execute("UPDATE artists SET net_worth = ?, age = ? WHERE name = ?", (net_worth, age, name))
                        conn.commit()
        else:
            print("Error:", response.status_code, response.text)
    print("finished")


def main():
    conn = sql.connect("junkies.db")
    cur = conn.cursor()
    print(get_artist_names(cur, conn))
    update_artist_table(get_artist_names(cur, conn), cur, conn)

if __name__ == "__main__":
    main()