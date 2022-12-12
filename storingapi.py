import sqlite3
import json
import os


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_tastedive_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS tastedive")
    cur.execute("CREATE TABLE tastedive (artist_id INTEGER, similar_artist_id INTEGER, media_type TEXT)")
    conn.commit()

def create_artists_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS artists")
    cur.execute("CREATE TABLE artists (artist_id INTEGER PRIMARY KEY, name TEXT, age INTEGER, net_worth INTEGER)")
    conn.commit()

def create_spotify_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS spotify")
    cur.execute("CREATE TABLE spotify (artist_id INTEGER PRIMARY KEY, popularity INTEGER, genre_id INTEGER)")
    conn.commit()

def create_genre_table(cur, conn):
    cur.execute("DROP TABLE IF EXISTS genre")
    cur.execute("CREATE TABLE genre (genre_id INTEGER PRIMARY KEY, genre_name TEXT)")
    conn.commit()



def main():
    cur, conn = setUpDatabase("junkies.db")
    create_tastedive_table(cur, conn)
    create_artists_table(cur, conn)
    create_spotify_table(cur, conn)
    create_genre_table(cur, conn)

if __name__ == "__main__":
    main()
