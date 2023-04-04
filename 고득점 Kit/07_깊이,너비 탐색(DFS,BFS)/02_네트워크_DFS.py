# DFS 
import sys 
sys.setrecursionlimit(10**6)

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

    # 연결된 노드를 그래프에 넣어준다.
    for i in range(len(computers)) :
        for j in range(len(computers)) :
            if i == j : 
                continue 
            if computers[i][j] == 1 and computers[j][i] == 1 :
                graph[i+1].append(j+1)

    # dfs 구현
    def dfs(v) :
        for curr_v in graph[v] :
            if not visited[curr_v] :
                visited[curr_v] = True 
                dfs(curr_v)

    # 네트워크 개수
    network_cnt = 0

    for i in range(1, n+1) :
        if not visited[i] :
            visited[i] = True 
            dfs(i)
            network_cnt += 1
    return network_cnt