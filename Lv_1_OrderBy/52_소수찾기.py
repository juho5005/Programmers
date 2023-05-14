INT_MAX = 1000001

is_prime = [True] * INT_MAX 
is_prime[0], is_prime[1] = False, False 

def solution(n):
    cnt = 0 

    for i in range(2, int((INT_MAX)**(1/2)) + 1) :
        j = 2
        if is_prime[j] : 
            while i * j < INT_MAX : 
                is_prime[i*j] = False 
                j += 1

    for k in range(2, n+1) :
        if is_prime[k] : 
            cnt += 1
    return cnt  