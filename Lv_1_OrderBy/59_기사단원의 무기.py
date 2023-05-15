def solution(number, limit, power):
    
    def cnt_of_prime(n) :
        cnt = 0
        for i in range(1, int(n ** (1/2)) + 1) :
            if n % i == 0 :
                if n//i == i :
                    cnt += 1
                else :
                    cnt += 2
        return cnt 
    
    res = 0

    for j in range(1, number+1) :
        x = cnt_of_prime(j)
        if x > limit :
            res += power 
        else :
            res += x   
    return res