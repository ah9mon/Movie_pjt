
# PJT 01

### 이번 pjt 를 통해 배운 내용

* get() 사용법 및 사용이유
* open() 사용법
* 리스트, 딕셔너리에 대하여 ,,
* 데이터 접근 및 추출 방법 

## A. 제공되는 영화 데이터의 주요내용 수집 (problem_a)

* 요구 사항 
  
  - 샘플 영화 데이터(movie.json)가 주어집니다.
    이중 서비스 구성에 필요한 정보만 추출해 반환하는 함수를 단계적으로 완성합니다.
    완성된 함수는 다음 문제의 기본 기능으로 사용됩니다.

* 결과  
  
  ```python
  {'genre_ids': [18, 80],
   'id': 278,
   'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누
  명을 쓴다. 주변의 증언과 살해 현장의 '
               '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같
  은 교도소 쇼생크로 향한다. 인간 말종 '
               '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 
  취급을 당한다. 그러던 어느 날, 간수의 '
               '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하 
  게 된다. 그 와중에 교도소 소장은 죄수들을 '
               '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려 
  주면서 그의 돈을 관리하는데...',
   'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
   'title': '쇼생크 탈출',
   'vote_average': 8.7}
  ```

* 문제 접근 방법 및 코드 설명

```python
import json
from pprint import pprint


def movie_info(movie):
    #pprint(movie)
    #id,title,poster_path,vote_average,overview,genre_ids 를 가져와야함
    rlt = {
        'id' : movie.get('id'), # 278
        'title' : movie.get('title'), # '쇼생크 탈출'
        'poster_path' : movie.get('poster_path'), # '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg' #해당 key가 있으면 해당 value 반환 / 없으면 None 반환 
        'vote_average' : movie.get('vote_average'), # 8.7
        'overview' : movie.get('overview'), #'촉망받는 어쩌구 ...'
        'genre_ids' : movie.get('genre_ids') #[18, 80]  
    }
    return rlt
```

* .get() 사용법 및 사용방법 배움

-----

## B.제공되는 영화 데이터의 주요내용 수정 (problem_b)

* 요구 사항
  
  - 이전 단계에서 만들었던 데이터 중 genre_ids를 장르 번호가 아닌 장르 이름 리스트
    genre_names로 바꿔 반환하는 함수를 완성합니다.
    완성된 함수는 다음 문제의 기본 기능으로 사용됩니다.

* 결과
  
  ```python
  {'genre_names': ['Crime', 'Drama'],
   'id': 278,
   'overview': '촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누
  명을 쓴다. 주변의 증언과 살해 현장의 '
               '그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같
  은 교도소 쇼생크로 향한다. 인간 말종 '
               '쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 
  취급을 당한다. 그러던 어느 날, 간수의 '
               '세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하 
  게 된다. 그 와중에 교도소 소장은 죄수들을 '
               '이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려 
  주면서 그의 돈을 관리하는데...',
   'poster_path': '/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg',
   'title': '쇼생크 탈출',
   'vote_average': 8.7}
  ```

* 문제 접근 방법 및 코드 설명

```python
import json
from pprint import pprint

# 'genre_ids': [18, 80]
def movie_info(movie, genres):

    #pprint(genres) 
    g_list = [] # []
    for index_num in range(len(genres)): # genres리스트의 원소 개수만큼 반복
        for g_id_num in movie['genre_ids']: # 쇼생크 탈출의 장르 아이디 리스트 원소꺼내며 반복
            if genres[index_num].get('id') == g_id_num: # 장르 리스트의 index_num번째 원소의 'id' 키의 벨류값과 쇼생크 탈출 장르 아이디가 같다면   
                g_list.append(genres[index_num].get('name')) # g_list = ['crime', 'drama']#g_list에 해당 장르명 추가

    #print(g_list)
    movie['genre_names'] = g_list #무비 딕셔너리에 'gente_names' : ['crime', 'drama'] 추가
    #pprint(movie)
    rlt = {
        'genre_names' : movie.get('genre_names'),
        'overview' : movie.get('overview'),
        'id' : movie.get('id'),
        'poster_path' : movie.get('poster_path'), # 해당 key가 있으면 해당 value 반환 / 없으면 None 반환 
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average'),
    }
    return rlt
```

* 딕셔너리 활용법

-----

## C.다중 데이터 분석 및 수정 (problem_c)

* 요구 사항
  
  - movies.json에는 평점이 높은 20개의 영화 데이터가 주어집니다.
    이 중 서비스 구성에 필요한 정보만 추출해 반환하는 함수를 완성합니다.
    완성된 함수는 향후 커뮤니티 서비스에서 제공되는 영화 목록을 제공하기 위한 기능
    으로 사용됩니다.

* 결과
  
  ```python
  너무 길어서 생략했습니다 
  ```

* 문제 접근 방법 및 코드 설명

```python
    import json
from pprint import pprint


def movie_info(movies, genres):
    top20_list = [] # []
    #pprint(movies)
    for i in range(len(movies)): # movies의 원소개수 만큼 반복 
        #print(movies[i]['title'])

        # 장르명 딕셔너리 생성
        g_list = [] # []
        for index_num in range(len(genres)): # genres리스트의 원소 개수만큼 반복
            for g_id_num in movies[i]['genre_ids']: # movies[i]의 장르 아이디 리스트 원소꺼내며 반복
                if genres[index_num].get('id') == g_id_num: # 장르 리스트의 index_num번째 원소의 'id' 키의 벨류값과 movies[i]의 장르 아이디가 같다면   
                    g_list.append(genres[index_num].get('name')) # g_list = ['crime', 'drama']#g_list에 해당 장르명 추가


        movies[i]['genre_names'] = g_list #무비 딕셔너리에 'gente_names' : ['crime', 'drama'] 추가


        # 영화 정보 리스트
        rlt = {
        'genre_names' : movies[i].get('genre_names'),
        'overview' : movies[i].get('overview'),
        'id' : movies[i].get('id'),
        'poster_path' : movies[i].get('poster_path'), 
        'title' : movies[i].get('title'),
        'vote_average' : movies[i].get('vote_average'),
        }
        top20_list.append(rlt) #최상위 for문이 끝날 때마다 movies[i]정보를 리스트에 담기
    return top20_list  
```

* for문을 활용해 많은 데이터에 접근해봄

-----

## D.알고리즘을 사용한 데이터 출력 (problem_d)

* 요구 사항
  
  - 영화 세부 정보 중 수입 정보(revenue)를 이용하여 모든 영화 중 가장 높은 수익을
    낸 영화를 출력하는 알고리즘을 작성합니다. 해당 과정은 향후 커뮤니티 서비스에서
    수익순으로 영화를 정렬하여 출력하는 정보로 사용됩니다.

* 결과 
  
  ```python
  반지의 제왕: 왕의 귀환
  ```

* 문제 접근 방법 및 코드 설명

```python
    import json
from pprint import pprint






def max_revenue(movies):
    revenue_dict = {} # 수익 딕셔너리
    revenue_list = [] # 수익 리스트 
    for i in range(len(movies)): # movies의 원소개수 만큼 반복
        num = movies[i]['id'] #movies에서 반복문을 사용해서 i번쨰 영화 id 추출 
        num_jason = open(f'data/movies/{num}.json', encoding='utf-8') #추출한id 로 movies 폴더 안의 id.json 실행
        num_jason_list = json.load(num_jason) #추출한id 로 movies 폴더 안의 id.json 실행
        # pprint(num_jason_list['revenue'])
        revenue_list.append(num_jason_list['revenue']) # 수익 리스트에 i번쨰 영화의 'revenue' 추가 
        revenue_dict[num_jason_list['revenue']] = num_jason_list['title'] # i번쨰 영화의 'revenue' : 'title' 딕셔너리 생성

    # print(revenue_dict) #{28341469: '쇼생크 탈출', 245066411: '대부', 321365567: '쉰들러 리스트', 357986087: '너의 이름은', 0: '청춘 돼지는 꿈꾸는 소녀의 꿈을 꾸지 않는다', 274925095: '센과 치히로의 행방불명', 257591776: '기생충', 286801374: '그린 마일', 214179088: '펄프 픽션', 230098753: '인생은 아름다워', 1118888979: '반지의 제왕: 왕의 귀환', 677387716: '포레스트 검프', 1004558444: '다크 나이트', 5472914: '원스 어폰 어 타임 인 아메리카', 11990401: '시네마 천 국', 100853753: '파이트 클럽', 30641770: '시티 오브 갓', 375540831: '스파이더맨: 뉴 유니버스', 236049757: '하울의 움직이는 성', 11000000: '위대한 독재자'}
    # pprint(revenue_list) 
    revenue_list.sort() # 오름차순으로 수익리스트 정렬 #[0, 5472914,11000000,11990401,28341469,30641770,100853753,214179088,230098753,236049757,245066411,257591776,274925095,286801374,321365567,357986087,375540831,677387716,1004558444,1118888979]
    #print(revenue_list[-1]) #1118888979
    #print(revenue_dict[revenue_list[-1]]) #반지의 제왕: 왕의 귀환
    max_revenue_movie = revenue_dict[revenue_list[-1]] #반지의 제왕: 왕의 귀환
    return max_revenue_movie #반지의 제왕: 왕의 귀환
    # 여기에 코드를 작성합니다.  movies.json에는 revenue에 대한 정보가 없어서 각 영화별로 더 디테일한 info에 접근하기 위해 data/movies/{movie_id}.json 파일에 접근해서 여기서 revenue 정보를 얻어냈다
```

* 함수 내부에서 사용할 일회용 빈딕셔너리 빈 리스트를 만들어서 활용했다
* open()/ load() 활용해봄

-----

## E.알고리즘을 사용한 데이터 출력 (problem_e)

* 요구 사항 
  
  - 영화 세부 정보 중 개봉일 정보(release_date)를 이용하여 모든 영화 중 12월에 개
    봉한 영화들의 제목 리스트를 출력하는 알고리즘을 작성합니다. 해당 과정은 향후 커
    뮤니티 서비스에서 추천 기능의 일부로 사용됩니다.

* 결과 
  
  ```python
  ['인생은 아름다워', '그린 마일', '반지의 제왕: 왕의 귀환', '스파이더맨: 뉴 유니버스
  ']
  ```

* 문제 접근 방법 및 코드 설명

```python
 import json



def dec_movies(movies):
    release_date_dict = {} #개봉일 딕셔너리
    release_date_list = [] # 개봉일 리스트
    dec_movies_list = [] # 12월 영화 리스트 
    for i in range(len(movies)): # movies의 원소개수 만큼 반복
        num = movies[i]['id'] #movies에서 반복문을 사용해서 id 추출 
        num_jason = open(f'data/movies/{num}.json', encoding='utf-8') #추출한id 로 movies 폴더 안의 id.json 가져오기
        num_jason_list = json.load(num_jason) #추출한id 로 movies 폴더 안의 id.json 가져오기

        release_date_list.append(num_jason_list['release_date']) # 개봉일 리스트에 'release_date' 추가
        release_date_dict[num_jason_list['release_date']] = num_jason_list['title'] # 개봉일 딕셔너리에 'release_date' : 'title' 추가

    release_date_list.sort() # 오름차순으로 개봉일 리스트 정렬
    # print(release_date_list) #['1940-10-23', '1972-03-14', '1984-05-23', '1988-11-17', '1993-11-30', '1994-07-06', '1994-09-10', '1994-09-23', '1997-12-20', '1999-10-15', '1999-12-10', '2001-07-20', '2002-02-05', '2003-12-01', '2004-11-19', '2008-07-16', '2016-08-26', '2018-12-06', '2019-05-30', '2019-06-15']
    # print(release_date_dict)  # {'1994-09-23': '쇼생크 탈출', '1972-03-14': '대부', '1993-11-30': '쉰들러 리스트', '2016-08-26': '너의 이름은', '2019-06-15': '청춘 돼지는 꿈꾸는 소녀의 꿈을 꾸지 않는다', '2001-07-20': '센과 치히로의 행방불명', '2019-05-30': '기생충', '1999-12-10': '그린 마일', '1994-09-10': '펄프 픽션', '1997-12-20': '인생은 아름다워', '2003-12-01': '반지의 제왕: 왕의 귀환', '1994-07-06': '포레스트 검프', '2008-07-16': '다크 나이트', '1984-05-23': '원스 어폰 어 타임 인 아메리카', '1988-11-17': '시네마 천국', '1999-10-15': '파이트 클럽', '2002-02-05': '시티 오브 갓', '2018-12-06': '스파이더맨: 뉴 유니버스', '2004-11-19': '하울의 움직이는 성', '1940-10-23': '위대한 독 재자'}
    for date in release_date_list: #개봉일 리스트의 원소에서 
        if date[5:7] == '12': # 12가 있다면 
            dec_movies_list.append(release_date_dict[date]) #12월 영화 리스트에 해당 영화이름 추가 
    #print(dec_movies_list)
    return dec_movies_list #['인생은 아름다워', '그린 마일', '반지의 제왕: 왕의 귀환', '스파이더맨: 뉴 유니버스']
```

* 4번과 비슷해서 비교적 손쉽게 진행했다 

# 후기

* 생각보다 어렵지 않았고 일주일간 배운 지식을 이용하면 어렵지않게 접근할 수 있었다
* 배운 것을 직접 활용해봐서 연습이 되었다
