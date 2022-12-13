import sqlite3
import json
import os


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_tastedive_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS tastedive (artist_id INTEGER, similar_artist_id INTEGER)")
    conn.commit()

def create_artists_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS artists (artist_id INTEGER PRIMARY KEY, name TEXT UNIQUE, age INTEGER, net_worth INTEGER)")
    conn.commit()

def create_spotify_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS spotify (artist_id INTEGER PRIMARY KEY, popularity INTEGER, genre_id INTEGER)")
    conn.commit()

def create_genre_table(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS genre (genre_id INTEGER PRIMARY KEY, genre_name TEXT UNIQUE)")
    conn.commit()

def table_reset(cur, conn):
    cur.execute("DROP TABLE IF EXISTS tastedive")
    cur.execute("DROP TABLE IF EXISTS artists")
    cur.execute("DROP TABLE IF EXISTS genre")
    cur.execute("DROP TABLE IF EXISTS spotify")
    conn.commit()


def main():
    cur, conn = setUpDatabase("junkies.db")

    # table_reset DELETES ALL TABLES
    # ONLY UNCOMMENT IF YOU WANT TO DELETE ALL DATA FROM THE DATABASE
    # table_reset(cur, conn)

    create_tastedive_table(cur, conn)
    create_artists_table(cur, conn)
    create_spotify_table(cur, conn)
    create_genre_table(cur, conn)
    # cur.execute("DELETE FROM artists WHERE artist_id > 106")
    # cur.execute("DELETE FROM tastedive WHERE artist_id = 3 OR artist_id = 1 OR artist_id = 70")
    # conn.commit()

if __name__ == "__main__":
    main()
