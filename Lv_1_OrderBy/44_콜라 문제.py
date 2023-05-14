def solution(a, b, n):
    res = 0
    extra = 0
    
    while (n//a) != 0 :
        x = n // a 
        res += x*b 
        
        extra = n % a 
        n = (x*b) + extra
    return res