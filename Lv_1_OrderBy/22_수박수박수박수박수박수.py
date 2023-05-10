def solution(n):
    flag = True 
    res = ''

    while n>0  :
        if flag :
            res += '수'
            flag = False
        else :
            res += '박'
            flag = True 
        n -= 1
    return res