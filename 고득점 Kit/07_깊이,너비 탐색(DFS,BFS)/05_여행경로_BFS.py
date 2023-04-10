from collections import deque

def solution(tickets) :
    # 가능한 모든 경로들의 집합
    answer = []

    # 큐 생성 
    q = deque()

    # 큐에 초기 값을 넣어줌
    # (현재 공항, 현재까지의 방문 경로들의 집합, 티켓을 사용했는가 인덱스로 판별)
    q.append(("ICN", ["ICN"], []))

    # 사용할 수 있는 티켓의 수
    l = len(tickets)

    # BFS
    while q :
        curr_airport, curr_passed, ticket_used = q.popleft()

        if len(ticket_used) == l :
            answer.append(curr_passed)
        
        for idx, ticket in enumerate(tickets) :
            if ticket[0] == curr_airport and idx not in ticket_used :
                q.append((ticket[1], curr_passed+[ticket[1]], ticket_used+[idx]))
    
    # 알파벳 순으로 먼저 방문한 공항순으로 정렬
    answer.sort()

    return answer[0]