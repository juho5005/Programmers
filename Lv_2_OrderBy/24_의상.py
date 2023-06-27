'''
1) 각 종류별로 최대 1가지 의상만 착용 가능
2) 착용한 의상이 일부가 겹치더라도, 다른 의상이 겹치지 않거나,
혹은 의상을 추가로 더 착용한 경우에는 서로 다른 방법으로 옷을 착용한 것으로 계산

3) 최소 한 개의 의상은 입어야 한다.

서로 다른 옷의 조합의 수의 개수는?
'''

def solution(clothes):
    dic = {}
    
    for cloth in clothes :
        if cloth[1] not in dic :
            dic[cloth[1]] = []
        dic[cloth[1]].append(cloth[0])
    
    res = 1
    
    for v in dic.values() :
        res *= (len(v) + 1) 
    
    res -= 1
    
    return res
    
print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))