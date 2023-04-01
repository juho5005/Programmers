from collections import deque

def solution(priorities, location):
    
    # 큐 생성
    idx_added_priorities = deque()
    for idx, elem in enumerate(priorities) :
        idx_added_priorities.append((elem, idx))

    # 몇 번째로 인식되는가 
    seq = 0 
    
    while idx_added_priorities :
        compare = idx_added_priorities.popleft()

        if any(compare[0] < imp[0] for imp in idx_added_priorities) :
            idx_added_priorities.append(compare)
        else :
            seq += 1
            if location == compare[1] :
                return seq 