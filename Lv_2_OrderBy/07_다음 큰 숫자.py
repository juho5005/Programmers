INT_MAX = 1000001

def solution(n):
    def binary_divide(num) :
        nums = []
        while num != 0 :
            nums.append(num%2)
            num = num//2
        
        return nums.count(1)
    
    l = binary_divide(n)
    
    for i in range(n+1, INT_MAX) :
        if l == binary_divide(i) :
            return i

print(solution(78))

    
    