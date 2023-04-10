import sys 
sys.setrecursionlimit(10**6)

def solution(tickets) :
    # 가능한 모든 경로들의 집합
    answer = []

    # 티켓을 사용했는가 안했는가를 판별할 vistied 배열
    visited = [
        False
        for _ in range(len(tickets))
    ]

    # 사용할 수 있는 티켓의 수
    l = len(tickets)

    def dfs(curr_airport, curr_passed) :
        if len(curr_passed) == l + 1 :
            answer.append(curr_passed)
            return # dfs 종료

        for idx, ticket in enumerate(tickets) :
            if curr_airport == ticket[0] and not visited[idx] :
                visited[idx] = True 
                dfs(ticket[1], curr_passed+[ticket[1]])
                visited[idx] = False 
    
    # dfs 실행
    dfs("ICN", ["ICN"])

    # 알파벳 순으로 먼저 방문한 공항순으로 정렬
    answer.sort()

    return answer[0]