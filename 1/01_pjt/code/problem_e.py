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
    
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
