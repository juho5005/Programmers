def solution(n):
    move = 0

    while n > 0 :
        # n이 짝수일 때
        if n%2 == 0 :
            n //= 2 
        
        # n이 홀수일 때
        else :
            n -= 1
            move += 1
    return move