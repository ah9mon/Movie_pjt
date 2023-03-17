import requests
from pprint import pprint

def popular_count():

    # 인기있는 영화 목록 데이터 요청 및 할당 
    URL = 'https://api.themoviedb.org/3/movie/popular'

    params = {
        'api_key' : '1395a6d8b9a1c30c3699c8181b8663a6',
        'language': 'ko',
        'region': 'KR',
    }
    
    response = requests.get(URL, params=params).json() # 인기있는 영화 목록 데이터 할당 
    # response = {'page' : 1, 'results' : [{영화 정보 1}, {영화 정보 2}, ..., {영화 정보 20}] ,... }
    
    # 몇개의 영화정보가 들어 있는 지 카운트 
    popular_movie_count = 0
    for movie_dict in response.get('results'): # 'results'의 value(영화정보 리스트)의 원소 하나 씩 꺼내서 반복 (20회)
        popular_movie_count += 1 # 1회 반복마다 + 1 해서 카운트함

    return popular_movie_count #20

  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
