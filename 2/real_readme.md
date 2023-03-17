>  PJT 작성 시 주의!
> 
> * 절대로 코드만 복붙하지 않는다.
> * 후기는 적어도 3줄은 씁시다!
> * 교수님이 안 볼 것 같지만 다 뜯어 봅니다.

# 

# PJT 01

### 이번 pjt 를 통해 배운 내용

* get() 사용법 및 사용이유
* open() 사용법
* 리스트, 딕셔너리에 대하여 ,,
* 데이터 접근 및 추출 방법 

## A. 인기 영화 조회 problem_a

* 요구 사항 
  
  - 인기 영화 목록을 응답 받아 개수를 출력합니다

* 결과  
  
  ```python
  20
  ```

* 문제 접근 방법 및 코드 설명

```python
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
```

* api 로 데이터 요청 및 할당하는 법 익히기 

-----

## B.특정 조건에 맞는 인기 영화 조회 1 problem_b

* 요구 사항
  
  - 인기 영화 목록 중 평점이 8 점 이상인 영화 목록을 출력합니다.

* 결과
  
  ```python
  [{'adult': False,
    'backdrop_path': '/faXT8V80JRhnArTAeYXz0Eutpv9.jpg',
    'genre_ids': [16, 28, 12, 35, 10751, 14],
    'id': 315162,
    'original_language': 'en',
    'original_title': 'Puss in Boots: The Last Wish',
    'overview': '아홉 개의 목숨 중 단 하나의 목숨만 남은 장화신은 고양이.  마지막 남은 목숨을 지키기  
  위해 히어로의 삶 대신 '
                '반려묘의 삶을 선택한 그에게 찾아온 마지막 기회, 바로 소원을 들어주는 소원별이 있는 곳
  을 알려주는 지도!  '
                "잃어버린 목숨을 되찾고 다시 히어로가 되기를 꿈꾸는 장화신은 고양이는 뜻밖에 동료가 된
   앙숙 파트너 '키티 "
                "말랑손', 그저 친구들과 함께라면 모든 게 행복한 강아지 '페로'와 함께 소원별을 찾기 위 
  해 길을 떠난다.  "
                '그리고 소원별을 노리는 또 다른 빌런들과 마주치게 되는데…',
    'popularity': 5946.788,
    'poster_path': '/rKgvctIuPXyuqOzCQ16VGdnHxKx.jpg',
    'release_date': '2023-01-04',
    'title': '장화신은 고양이: 끝내주는 모험',
    'video': False,
    'vote_average': 8.6,
    'vote_count': 2658},
   {'adult': False,
    'backdrop_path': '/e782pDRAlu4BG0ahd777n8zfPzZ.jpg',
    'genre_ids': [16, 14, 18],
    'id': 555604,
    'original_language': 'en',
    'original_title': "Guillermo del Toro's Pinocchio",
    'overview': '많은 이들의 사랑을 받은 목각 인형 피노키오의 마법 같은 모험. 현실의 한계를 뛰어넘어, 
  새 생명을 불어넣는 '
                '강력한 사랑의 힘이 펼쳐진다. 이탈리아 고전 동화 "피노키오"가 스톱모션 뮤지컬로 재탄생
  한다. 말썽꾸러기 '
                '피노키오는 과연 인간 소년이 될 수 있을까? 그 여정을 따라가 보자.',
    'popularity': 727.871,
    'poster_path': '/6bdUtxydFXLtgcxHMMvlkNnRZWg.jpg',
    'release_date': '2022-11-23',
    'title': '기예르모 델토로의 피노키오',
    'video': False,
    'vote_average': 8.4,
    'vote_count': 1666}]
  ```

* 문제 접근 방법 및 코드 설명

```python
import json
import requests
from pprint import pprint

def vote_average_movies():
    # 인기있는 영화 목록 데이터 요청 및 할당 
    URL = 'https://api.themoviedb.org/3/movie/popular'

    params = {
        'api_key' : '1395a6d8b9a1c30c3699c8181b8663a6',
        'language': 'ko',

        'region' : 'KR'
    }

    response = requests.get(URL, params=params).json() # 인기있는 영화 목록 데이터 할당 
    # response = {'page' : 1, 'results' : [{영화 정보 1}, {영화 정보 2}, ..., {영화 정보 20}] ,... }

    # 평점 8점 이상인 영화 목록을 반복문으로 반환 
    over_8_movies = []
    for movie_dict in response.get('results'): # 'results'의 value(영화정보 리스트)의 원소 하나 씩 꺼내서 반복 (20회)
        if movie_dict.get('vote_average') >= 8: # 만약 movie_dict의 'vote_average' key의 value값이 8 이상이면
            over_8_movies.append(movie_dict) #over_8_movies 리스트에 영화 정보 추가 

    return over_8_movies
```

* api 실습 

-----

## C.특정 조건에 맞는 인기 영화 조회 2 problem_c

* 요구 사항
  
  - 인기 영화 목록을 평점이 높은 순으로 5 개의 영화 데이터 목록 출력합니다다.

* 결과
  
  ```python
  [{'adult': False,
    'backdrop_path': '/faXT8V80JRhnArTAeYXz0Eutpv9.jpg',
    'genre_ids': [16, 28, 12, 35, 10751, 14],
    'id': 315162,
    'original_language': 'en',
    'original_title': 'Puss in Boots: The Last Wish',
    'overview': '아홉 개의 목숨 중 단 하나의 목숨만 남은 장화신은 고양이.  마지막 남은 목숨을 지키기  
  위해 히어로의 삶 대신 '
                '반려묘의 삶을 선택한 그에게 찾아온 마지막 기회, 바로 소원을 들어주는 소원별이 있는 곳
  을 알려주는 지도!  '
                "잃어버린 목숨을 되찾고 다시 히어로가 되기를 꿈꾸는 장화신은 고양이는 뜻밖에 동료가 된
   앙숙 파트너 '키티 "
                "말랑손', 그저 친구들과 함께라면 모든 게 행복한 강아지 '페로'와 함께 소원별을 찾기 위 
  해 길을 떠난다.  "
                '그리고 소원별을 노리는 또 다른 빌런들과 마주치게 되는데…',
    'popularity': 5946.788,
    'poster_path': '/rKgvctIuPXyuqOzCQ16VGdnHxKx.jpg',
    'release_date': '2023-01-04',
    'title': '장화신은 고양이: 끝내주는 모험',
    'video': False,
    'vote_average': 8.6,
    'vote_count': 2658},
   {'adult': False,
    'backdrop_path': '/e782pDRAlu4BG0ahd777n8zfPzZ.jpg',
    'genre_ids': [16, 14, 18],
    'id': 555604,
    'original_language': 'en',
    'original_title': "Guillermo del Toro's Pinocchio",
    'overview': '많은 이들의 사랑을 받은 목각 인형 피노키오의 마법 같은 모험. 현실의 한계를 뛰어넘어, 
  새 생명을 불어넣는 '
                '강력한 사랑의 힘이 펼쳐진다. 이탈리아 고전 동화 "피노키오"가 스톱모션 뮤지컬로 재탄생
  한다. 말썽꾸러기 '
                '피노키오는 과연 인간 소년이 될 수 있을까? 그 여정을 따라가 보자.',
    'popularity': 727.871,
    'poster_path': '/6bdUtxydFXLtgcxHMMvlkNnRZWg.jpg',
    'release_date': '2022-11-23',
    'title': '기예르모 델토로의 피노키오',
    'video': False,
    'vote_average': 8.4,
    'vote_count': 1666},
   {'adult': False,
    'backdrop_path': '/s16H6tpK2utvwDtzZ8Qy4qm5Emw.jpg',
    'genre_ids': [878, 12, 28],
    'id': 76600,
    'original_language': 'en',
    'original_title': 'Avatar: The Way of Water',
    'overview': '판도라 행성에서 제이크 설리와 네이티리가 이룬 가족이 겪게 되는 무자비한 위협과 살아남
  기 위해 떠나야 하는 긴 '
                '여정과 전투, 그리고 견뎌내야 할 상처에 대한 이야기를 그렸다. 살아남기 위해 설리 가족 
  이 숲에서 바다로 터전을 '
                '옮기면서 겪게 되는 화합의 과정, 그리고 곳곳에서 도사리는 새로운 위협까지 역경 속에서 
  더 아름답게 펼쳐진다.',
    'popularity': 2391.76,
    'poster_path': '/z56bVX93oRG6uDeMACR7cXCnAbh.jpg',
    'release_date': '2022-12-14',
    'title': '아바타: 물의 길',
    'video': False,
    'vote_average': 7.7,
    'vote_count': 4671},
   {'adult': False,
    'backdrop_path': '/8I37NtDffNV7AZlDa7uDvvqhovU.jpg',
    'genre_ids': [28, 12, 14, 878],
    'id': 19995,
    'original_language': 'en',
    'original_title': 'Avatar',
    'overview': '가까운 미래, 지구는 에너지 고갈 문제를 해결하기 위해 머나먼 행성 판도라에서 대체 자원
  을 채굴하기 시작한다. '
                '하지만 판도라의 독성을 지닌 대기로 인해 자원 획득에 어려움을 겪게 된 인류는 판도라의 
  토착민 나비의 외형에 '
                '인간의 의식을 주입, 원격 조종이 가능한 새로운 생명체를 탄생시키는 프로그램을 개발한다
  . 한편 하반신이 마비된 '
                '전직 해병대원 제이크 설리는 아바타 프로그램에 참가할 것을 제안받는다. 그 곳에서 자신 
  의 아바타를 통해 자유롭게 '
                '걸을 수 있게 된 제이크는 자원 채굴을 막으려는 나비의 무리에 침투하라는 임무를 부여받 
  는데...',
    'popularity': 1145.042,
    'poster_path': '/zygmx5abXeDpr3fWYX4jlXFZ1wh.jpg',
    'release_date': '2009-12-17',
    'title': '아바타',
    'video': False,
    'vote_average': 7.6,
    'vote_count': 28031},
   {'adult': False,
    'backdrop_path': '/yYrvN5WFeGYjJnRzhY0QXuo4Isw.jpg',
    'genre_ids': [28, 12, 878],
    'id': 505642,
    'original_language': 'en',
    'original_title': 'Black Panther: Wakanda Forever',
    'overview': '국왕이자 블랙 팬서인 티찰라의 죽음 이후 수많은 강대국으로부터 위협을 받게 된 와칸다. 
  라몬다, 슈리 그리고 '
                '나키아, 오코예, 음바쿠는 각자 사명감을 갖고 와칸다를 지키기 위해 외로운 싸움을 이어간
  다. 한편, 비브라늄의 '
                '패권을 둘러싼 미스터리한 음모와 함께 깊은 해저에서 모습을 드러낸 최강의 적 네이머와  
  탈로칸의 전사들은 와칸다를 '
                '향해 무차별 공격을 퍼붓기 시작하는데…',
    'popularity': 1216.323,
    'poster_path': '/3PCRWLeqp5y20k6XVzcamZR3BWF.jpg',
    'release_date': '2022-11-09',
    'title': '블랙 팬서: 와칸다 포에버',
    'video': False,
    'vote_average': 7.5,
    'vote_count': 1694}]
  ```

* 문제 접근 방법 및 코드 설명

```python
import requests
from pprint import pprint


def ranking():
    # 인기있는 영화 목록 데이터 요청 및 할당 
    URL = 'https://api.themoviedb.org/3/movie/popular'

    params = {
        'api_key' : '1395a6d8b9a1c30c3699c8181b8663a6',
        'language': 'ko',
        'region': 'KR',
    }

    response = requests.get(URL, params=params).json() # 인기있는 영화 목록 데이터 할당 
    # response = {'page' : 1, 'results' : [{영화 정보 1}, {영화 정보 2}, ..., {영화 정보 20}] ,... }

    # 평점 높은 순으로 내림차순 정렬 후 상위 5개 영화 리스트로 반환
    movies_list = response.get('results') # [{영화 정보 1}, {영화 정보 2}, ..., {영화 정보 20}]
    movies_list.sort(key = lambda x : x.get('vote_average'), reverse = True) # movies_list를 평점 높은 순으로 내림차순 정렬 
    return movies_list[0:5] # 상위 5개 리턴
```

* sort로 리스트 정렬 실습 

-----

## D.특정 추천 영화 조회 problem_d

* 요구 사항
  
  - 제공된 영화 제목 기생충 그래비티 검색할 수 없는 영화 을 검색하여
    추천 영화 목록을 출력합니다결과 

* ```python
  ['그린 북',
   'Awdat Al-Rouh',
   '조커',
   '원스 어폰 어 타임 인… 할리우드',
   '1917',
   '조조 래빗',
   'My Chemical Romance: AOL Sessions',
   'Back Home',
   '결혼 이야기',
   '나이브스 아웃',
   '대부',
   '아이리시맨',
   '센과 치히로의 행방불명',
   'The Wrestling Classic',
   'Shanghai Fever',
   '포드 V 페라리',
   '너의 이름은',
   '쇼생크 탈출',
   'Is Sumiyati Going to Hell?',
   '작은 아씨들',
   '펄프 픽션']
  []
  None
  ```

* 문제 접근 방법 및 코드 설명

```python
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
```

* api 활용 실습 및 딕셔너리 데이터 활용

-----

## E.출연진 연출진 데이터 조회 problem_e

* 요구 사항 
  
  - 제공된 영화 제목 기생충 검색할 수 없는 영화 을 검색하여
    해당 영화의 출연진(cast) 과 스태프 (crew) 중 연출진 (Directing)의 이름 출력합니다

* 결과 
  
  ```python
  {'cast': ['Song Kang-ho',
            'Lee Sun-kyun',
            'Cho Yeo-jeong',
            'Choi Woo-shik',
            'Park So-dam',
            'Lee Jung-eun',
            'Jang Hye-jin'],
   'directing': ['Bong Joon-ho',
                 'Park Hyun-cheol',
                 'Han Jin-won',
                 'Kim Seong-sik',
                 'Lee Jung-hoon',
                 'Yoon Young-woo']}
  None
  ```

* 문제 접근 방법 및 코드 설명

```python
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
```

* api 실습 및 딕셔너리 활용  

# 후기

* api는 이름만 들어보고 실제로 사용하기 어렵다고 생각해서 학부시절 프로젝트 때 활용하지 않았었는데 생각보다 어렵지 않아서 좀 더 익숙해지면 편하게 사용할 것 같다 
