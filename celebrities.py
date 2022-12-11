import requests
import sqlite3 as sql
import json
'''
celebrities = []

for i in celebrities:
    api_url = 'https://api.celebrityninjas.com/v1/search?name='
    name = "Beyonce"
    response = requests.get(api_url + name, headers={'X-Api-Key': 'QU/Mur5QkwH5le8q3vJXAw==DMX06hqjhQmyHZ4T'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
'''
def get_artist_names(cur, conn):
    cur.execute("SELECT name FROM artists")
    artist_list = cur.fetchall()
    artists = [x[0] for x in artist_list]
    return artists

def update_artist_table(artists, cur, conn):
    worths = []
    ages = []
    for i in artists:
        name = i
        api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name)
        response = requests.get(api_url, headers={'X-Api-Key': 'QU/Mur5QkwH5le8q3vJXAw==ZePF0pHAnt3Lx2nO'})
        if response.status_code == requests.codes.ok:
            js = json.loads(response.text)
        else:
            print("Error:", response.status_code, response.text)
        for items in js:
            net_worth = items['net_worth']
            #age = int(items['age'])
            worths.append(net_worth)
            #ages.append(age)
    for values in worths:
        cur.execute("INSERT OR IGNORE INTO artists (net_worth) VALUES (?)" (int(values), ))
        conn.commit()
    #for numbers in ages:
        #cur.execute("INSERT OR IGNORE INTO artists (age) VALUES (?)" (numbers, ))
        #conn.commit()



def main():
    conn = sql.connect("junkies.db")
    cur = conn.cursor()
    get_artist_names(cur, conn)
    update_artist_table(get_artist_names(cur, conn), cur, conn)

if __name__ == "__main__":
    main()
