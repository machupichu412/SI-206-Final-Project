import requests

celebrities = []

for i in celebrities:
    api_url = 'https://api.celebrityninjas.com/v1/search?name='
    name = "Beyonce"
    response = requests.get(api_url + name, headers={'X-Api-Key': 'QU/Mur5QkwH5le8q3vJXAw==DMX06hqjhQmyHZ4T'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)