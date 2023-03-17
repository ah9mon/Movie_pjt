import requests
from pprint import pprint


def recommendation(title):
    # 인기있는 영화 목록 데이터 요청 및 할당 
    URL = 'https://api.themoviedb.org/3/search/movie'

    params = {
        'api_key' : '1395a6d8b9a1c30c3699c8181b8663a6',
        'language': 'ko',
        'region': 'KR',
        'query' : title
            
    }
    
    response1 = requests.get(URL, params=params).json()  
    # response1 = {'page' : 1, 'results' : [{영화 정보 1}, {영화 정보 2}, ..., {영화 정보 20}] ,... }
    
    movie_list = response1.get('results')
    
    if movie_list == []: # movie_list가 빈 리스트이면 (영화 검색이 안되면) 
        return None #None
        
    # 해당 영화의 id값 변수에 할당 
    movie_id = movie_list[0].get('id')
    
    # 추천 영화 목록 데이터 요청 및 할당
    URL = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'

    params = {
        'api_key' : '1395a6d8b9a1c30c3699c8181b8663a6',
        'language': 'ko',
        'region': 'KR'
            
    }
    response2 = requests.get(URL, params=params).json()
    # response2 = {'page' : 1, 'results' : [{영화 정보 1}, {영화 정보 2}, ..., {영화 정보 20}] ,... }
    
    # 추천받은 영화 목록 생성 및 반환
    recommended_movies = []
    for index_dict in response2.get('results'): # response2의 'results'의 value(추천 영화 목록)의 항목들을 꺼내서 반복
        recommended_movies.append(index_dict.get('title')) # 각 항목의 영화 제목을 recommended_movies 리스트에 담기


    return recommended_movies

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
