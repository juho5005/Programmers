def solution(n):
    ternary = ''

    while n != 0 :
        ternary = str(n%3) + ternary 
        n //= 3 
    
    res = 0
    interval = 0
    for elem in ternary :
        res += int(elem) * (3 ** interval)
        interval += 1
    
    return res 