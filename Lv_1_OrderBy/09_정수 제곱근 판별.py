def solution(n):
    sqrt_n = n**(1/2)

    if int(sqrt_n) ** 2 == n :
        return int((sqrt_n+1) ** 2) 
    else :
        return -1