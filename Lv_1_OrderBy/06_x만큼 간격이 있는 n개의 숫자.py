def solution(x, n):
    ans = []
    interval = x

    for _ in range(n) :
        ans.append(x)
        x += interval 
    
    return ans