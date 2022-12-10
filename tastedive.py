import requests
import json

accesskey = "445402-SpotifyJ-NH86KIWN"

def get_artist_from_tastedive(name):
    url = 'https://tastedive.com/api/similar'
    param = {}

    param['q'] = name
    param['type'] = 'music'
    param['limit'] = 25
    param['k'] = accesskey

    r = requests.get(url,params=param)
    js = json.loads(r.text)
    return js

def main():
    print(get_artist_from_tastedive("Drake"))

if __name__ == "__main__":
    main()
