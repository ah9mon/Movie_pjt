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
     # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
