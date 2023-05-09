def solution(a, b):
    if a == b :
        return a 

    res = 0

    if a < b :
        for i in range(a, b+1) :
            res += i 
    else :
        for i in range(b, a+1) :
            res += i   
    return res 