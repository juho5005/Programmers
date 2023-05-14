'''
k : 사과의 최대 점수
m : 한 상자에 들어가는 사과의 수
score : 사과들의 점수
'''

def solution(k, m, score):
    l = len(score) # 사과의 총 개수
    
    # 만들 수 있는 상자의 개수
    c = l // m 

    score.sort(reverse=True) # 내림차순 정렬 

    idx = 0
    res = 0 
    while c : 
        min_score = min(score[idx:idx+m])
        res += min_score * m
        c -= 1
        idx += m
    return res 