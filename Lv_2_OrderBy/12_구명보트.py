from collections import deque  
def solution(people, limit):
    people.sort() # 오름차순으로 정렬
    # deque으로 만들어줌
    deq_people = deque(people)

    cnt = 0

    while deq_people :
        if len(deq_people) == 1:
            cnt += 1
            break 

        min_p = deq_people[0]
        max_p = deq_people[-1]

        if (min_p + max_p) <= limit :
            deq_people.popleft()
            deq_people.pop()
            cnt += 1
            continue 
        
        deq_people.pop()
        cnt += 1

    return cnt 

print(solution([70, 80, 50], 100))