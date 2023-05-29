INT_MAX = 100001

def solution(n):
    dp = [0, 1]

    for i in range(2, INT_MAX+1) :
        dp.append((dp[i-1] + dp[i-2])%1234567)

        if i == n :
            return dp[-1]
    
print(solution(5))