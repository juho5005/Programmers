from collections import deque 

def solution(numbers, target):
    # 정답의 개수
    cnt = 0
    
    # 덱 생성
    q = deque()

    # 덱의 인자로 (현재까지의 합, 인덱스)를 넣어줌
    q.append((0, 0))

    # bfs
    while q : 
        curr_sum, curr_idx  = q.popleft()

        if curr_idx == len(numbers) :
            if curr_sum == target :
                cnt += 1
        
        else :
            curr_num = numbers[curr_idx]
            
            q.append((curr_sum + curr_num, curr_idx + 1))
            q.append((curr_sum - curr_num, curr_idx + 1))
    
    return cnt
            


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))