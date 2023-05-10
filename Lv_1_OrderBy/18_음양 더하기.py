def solution(absolutes, signs):
    res = 0
    for num, sign in zip(absolutes, signs) :
        if sign == True :
            res += num
        else :
            res -= num 
    return res 