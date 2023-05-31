def solution(arr):
    min_lcm = arr[0]

    # 최대 공약수
    def gcd(a, b) :
        while b > 0 :
            a, b = b, a%b 
        return a 

    # 최소 공배수
    def lcm(a, b) :
        return a * b // gcd(a,b)
    
    
    for i in range(1, len(arr)) :
        min_lcm = lcm(min_lcm, lcm(min_lcm, arr[i]))
    return min_lcm

print(solution([2, 6, 8, 14]))