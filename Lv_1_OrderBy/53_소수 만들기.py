def solution(nums):
    def is_prime(n) :
        for i in range(2, n) :
            if n % i == 0 :
                return False 
        return True
    
    cnt = 0

    l = len(nums)    
    for i in range(l) :
        for j in range(i+1, l) :
            for k in range(j+1, l) :
                if is_prime(nums[i] + nums[j] + nums[k]) :
                    cnt += 1
    return cnt 