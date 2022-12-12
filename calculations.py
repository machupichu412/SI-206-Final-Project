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
    
    return total/count

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

def avg_net_worth_by_genre_vis(cur, conn):
    genres = get_genre_list(cur, conn)
    max_names = []
    max_net_worths = []
    min_names = []
    min_net_worths = []
    avg = []
    for genre in genres:
        max_net_worth, max_name = max_networth_genre(genre, cur, conn)
        min_net_worth, min_name = min_networth_genre(genre, cur, conn)
        avg_for_genre = avg_networth_genre(genre, cur, conn)
        max_names.append(max_name)
        max_net_worths.append(max_net_worth)
        min_names.append(min_name)
        min_net_worths.append(min_net_worth)
        avg.append(avg_for_genre)

    plt.figure()
    plt.scatter(x=genres, y=avg)
    plt.scatter(x=genres, y=max_net_worths, c='r', marker='x')
    plt.scatter(x=genres, y=min_net_worths, c='r', marker='x')

    for i, txt in enumerate(max_names):
        plt.annotate(txt, (genres[i], max_net_worths[i]))

    for i, txt in enumerate(min_names):
        plt.annotate(txt, (genres[i], min_net_worths[i]))

    plt.xlabel("music genre")
    plt.ylabel("net worth (USD)")
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.xticks(rotation=45, ha='right')
    plt.show()

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

def net_worth_by_genre_vis(cur, conn):
    # threeway join
    # cur.execute("SELECT artists.net_worth, genre.genre_name FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 OR artists.net_worth IS NOT NULL")
    genre_net_worths = {}

    genres = get_genre_list(cur, conn)

    for genre in genres:
        cur.execute("SELECT artists.net_worth FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id JOIN genre ON spotify.genre_id = genre.genre_id WHERE artists.net_worth != -1 AND artists.net_worth IS NOT NULL AND genre.genre_name = ?", (genre,))
        net_worths = cur.fetchall()
        net_worths = [x[0] for x in net_worths]
        genre_net_worths[genre] = net_worths

    fig, ax = plt.subplots()
    ax.boxplot(genre_net_worths.values())
    ax.set_xticklabels(genre_net_worths.keys())

    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.ylabel("artist net worth (USD)")
    plt.xlabel("music genre")
    plt.xticks(rotation = 30)
    plt.yticks(rotation = 30)
    plt.tight_layout()
    plt.show()

def popularity_vs_net_worth(cur, conn):
    cur.execute("SELECT artists.net_worth, spotify.popularity, artists.name FROM artists JOIN spotify ON artists.artist_id = spotify.artist_id WHERE artists.net_worth != -1 AND artists.net_worth IS NOT NULL")
    networthpoplist = cur.fetchall()

    net_worth = []
    popularity =[]
    name = []
    for item in networthpoplist:
        net_worth.append(item[0])
        popularity.append(item[1])
        name.append(item[2])

    plt.figure()
    plt.scatter(popularity, net_worth)
    

    for i, txt in enumerate(name):
        plt.annotate(txt, (popularity[i], net_worth[i]))

    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.ylabel("net worth (USD)")
    plt.xlabel("Spotify popularity score")
    plt.xticks(rotation=45, ha='right')
    plt.show()


def main():
    conn = sql.connect("junkies.db")
    cur = conn.cursor()
    valid = True
    userInput = int(input("Enter a visualization option (1-3): "))
    while valid:
        if userInput == 1:
            net_worth_by_genre_vis(cur, conn)
            break
        elif userInput == 2:
            popularity_vs_net_worth(cur, conn)
            break
        elif userInput == 3:
            avg_net_worth_by_genre_vis(cur, conn)
            break
        else:
            print("Not a valid input!")
            userInput = int(input("Enter a visualization option (1-3): "))

if __name__ == "__main__":
    main()    