import sys 
sys.setrecursionlimit(10**6)

# 정답의 개수
cnt = 0

def solution(numbers, target):
    # DFS
    def dfs(curr_sum, curr_idx) :
        global cnt
        if curr_idx == len(numbers) :
            if curr_sum == target :
                cnt += 1
                return 
        
        else :
            curr_num = numbers[curr_idx]
            dfs(curr_sum+curr_num, curr_idx+1)
            dfs(curr_sum-curr_num, curr_idx+1)            
    
    # (0, 0)으로 시작
    dfs(0, 0)

    return cnt