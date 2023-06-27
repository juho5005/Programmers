'''
DB캐시를 적용할 때 캐시 크기에 따른 실행시간을 측정

condition)
1 -> 대소문자 구분 X
2 -> 도시 이름은 최대 20자

Cache HIT => 1
Cache MISS => 5

'''
from collections import deque 

def solution(cacheSize, cities):
    # 캐시의 크기가 0인 경우 => 어차피 모든 경우 Cache Miss이다.
    if cacheSize == 0 :
        return 5 * len(cities)
    
    # 캐시의 크기가 1이 아닌 경우
    dq = deque()

    # 정답 
    res = 0

    for city in cities :
        # 대소문자를 구별하지 않음 [소문자로 고정]
        city = city.lower()

        # city가 dq안에 존재할 때 [Cache Hit]
        if city in dq : 
            res += 1
            dq.remove(city)
            dq.append(city)
        
        # city가 dq안에 존재하지 않을 때 [Cache Miss]
        else :
            res += 5
            
            # 만약 캐시가 다 차지 않은 경우
            if len(dq) < cacheSize :
                dq.append(city)
            
            # 만약 캐시가 다 찬 경우
            else :
                dq.popleft()
                dq.append(city)
    
    return res