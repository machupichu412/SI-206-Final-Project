import math

def avg_networth_genre(genrename):
    genre_dict = {}
    networth = 0
    count = 0
    
    for genre in genre_dict:
        if genre['genre_name'] = genrename:
            networth += genre['Networth']
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
        if genre['genre_name'] = genrename:
            popularity += genre['Popularity']
            count += 1

    return popularity/count
