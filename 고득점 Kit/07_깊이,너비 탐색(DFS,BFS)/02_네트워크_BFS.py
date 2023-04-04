# BFS 
from collections import deque 

def solution(n, computers) :
    # 그래프 생성
    graph = [
        []
        for _ in range(n+1)
    ]

    # 방문여부 생성
    visited = [
        False 
        for _ in range(n+1)
    ]

    # 큐 생성
    q = deque()

    # 연결된 노드를 그래프에 넣어준다.
    for i in range(len(computers)) :
        for j in range(len(computers)) :
            if i == j : 
                continue 
            if computers[i][j] == 1 and computers[j][i] == 1 :
                graph[i+1].append(j+1)

    # bfs 구현
    def bfs() :
        while q : 
            curr_v = q.popleft()

            for next_v in graph[curr_v] :
                if not visited[next_v] :
                    visited[next_v] = True
                    q.append(next_v)

    # 네트워크의 개수를 세주기
    network_cnt = 0

    for i in range(1, n+1) :
        if not visited[i] :
            visited[i] = True 
            q.append(i)
            bfs()
            network_cnt += 1

    return network_cnt