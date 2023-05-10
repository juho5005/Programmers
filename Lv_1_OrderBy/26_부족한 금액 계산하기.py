def solution(price, money, count):
    res = 0
    interval = price

    for _ in range(count) :
        res += interval 
        interval += price 
    
    if res < money :
        return 0 
    else :
        return res - money