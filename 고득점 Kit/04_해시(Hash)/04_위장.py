def solution(clothes):
    dic = {}

    for cloth in clothes : 
        if cloth[-1] not in dic :
            dic[cloth[-1]] = 1
        else :
            dic[cloth[-1]] += 1
    
    # 결과 값
    res = 1

    if len(dic.items()) == 1 : # 한 종류만 있다면
        for e in dic.keys() :
            return dic[e]
    else :
        for k, v in dic.items() :
            res *= (v+1)
        res -= 1
        return res