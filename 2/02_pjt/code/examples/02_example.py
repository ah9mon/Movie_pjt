# requests 사용 예시 2

import requests


URL = 'https://api.themoviedb.org/3/movie/popular'

params = {
    'api_key' : '1395a6d8b9a1c30c3699c8181b8663a6',
    'language': 'en-US',
    'page': '1',
}

response = requests.get(URL, params=params).json()
print(response)
