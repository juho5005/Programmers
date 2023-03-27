def solution(people, limit):
    # 오름차순 정렬
    people.sort()
    
    # 필요한 보트의 수 
    boat_cnt = 0

    start = 0 
    end = len(people) - 1

    while start <= end :
        if people[end] + people[start] <= limit :
            start += 1 
        boat_cnt += 1
        end -= 1

    return boat_cnt
