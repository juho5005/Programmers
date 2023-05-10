def solution(left, right):
    res = 0 

    def count_prime_num(num) :
        cnt = 0
        for i in range(1, num+1) :
            if num % i == 0 :
                cnt += 1
        return cnt 
    
    for j in range(left, right+1) :
        if count_prime_num(j) % 2 == 0:
            res += j 
        else :
            res -= j 
            
    return res