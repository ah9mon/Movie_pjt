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
    # 여기에 코드를 작성합니다.    








# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
