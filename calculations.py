import math
import sqlite3 as sql
import matplotlib.pyplot as plt

# def calculate_data(cur, conn):
#     cur.execute("SELECT Avg(net_worth) from artists JOIN spotify on artists.artist_id = spotify.artist_id where spotify.genre_id = '1'")
#     cur.execute("SELECT Avg (age) from artists JOIN spotify on artists.artist id = spotify.artist_id group by spotify.genre_id")
#     cur.execute("SELECT count(age) from artists where artists.age < '20'")
#     cur.execute("SELECT count (age) from artists where artists.age >'50'")
#     cur.execute("SELECT artists.name, artists.net_worth, spotify.popularity, genre.genre_name from artists JOIN spotify on artists.artist_id = spotify-artist_id JOIN genre on spotify.genre_id = genre.genre_id ORDER BY artists.net worth LIMIT 10")

def get_genre_list(cur, conn):
    cur.execute("SELECT genre_name FROM genre")
    genres = cur.fetchall()
    genres = [x[0] for x in genres]
    return genres

def avg_networth_genre(genrename, cur, conn):
    total = 0
    count = 0

    cur.execute("SELECT artists.net_worth FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 AND artists.net_worth IS NOT NULL AND genre.genre_name = ?", (genrename,))
    networths = [x[0] for x in cur.fetchall()]
    for networth in networths:
        total += networth
        count += 1
    
    return networth/count

def correlation_age_networth(data):
    age = []
    networth = []
    age_total = 0
    networth_total = 0
    count = 0

    for age_value in age:
        age_total += age_value
        for networth_value in networth:
            networth_total += networth_value
            count += 1

    age_avg = age_total / count
    networth_avg = networth_total / count

    covariance = 0
    for age_value in age:
        for networth_value in networth:
            point = (age_value - age_avg) * (networth_value - networth_avg)
            covariance += point

    return covariance / (count - 1)

def avg_popularity_genre(genrename):
    genre_dict = {}
    popularity = 0
    count = 0
    
    for genre in genre_dict:
        if genre['genre_name'] == genrename:
            popularity += genre['Popularity']
            count += 1

    return popularity/count
