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
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

