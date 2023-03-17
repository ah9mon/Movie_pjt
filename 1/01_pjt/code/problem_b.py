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

    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    #pprint(genres_json)
    genres_list = json.load(genres_json)
    #pprint(genres_list)
    pprint(movie_info(movie, genres_list))