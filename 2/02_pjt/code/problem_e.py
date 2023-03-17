import requests
from pprint import pprint


def credits(title):
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

    # 출연진과 스태프 목록 요청 및 할당
    URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'

    params = {
        'api_key' : '1395a6d8b9a1c30c3699c8181b8663a6',
        'language': 'ko',
        'region': 'KR'
            
    }
    response2 = requests.get(URL, params=params).json()
   

    # cast_id값이 10미만인 출연진만 추출
    under_10_casts = []
    cast_list = response2.get('cast') # cast 리스트만 꺼내서 할당
    for cast in cast_list: # cast 리스트에서 cast 정보 딕셔너리(항목) 마다 
        if cast.get('cast_id') < 10: # cast 딕셔너리 내의 'cast_id' 벨류 값이 10 미만이면 
            under_10_casts.append(cast.get('name')) # 이름을 10미만 리스트에 추가 
    
    # department가 Directing인 데이터만 추출
    directing_crew = []
    crew_list = response2.get('crew') # crew 리스트만 꺼내서 할당
    for crew in crew_list: # crew 리스트의 crew 정보 딕셔너리(항목) 마다 
        if crew.get('department') == 'Directing': # crew의 department가 디렉팅이면
            directing_crew.append(crew.get('name')) # 디렉팅 리스트에 이름 추가 
        
    members = {'cast' : under_10_casts, 'directing' : directing_crew}

    return members

    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
