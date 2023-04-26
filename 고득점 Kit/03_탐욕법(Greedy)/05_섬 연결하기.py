"""
n개의 섬 사이에 다리를 건설하는 비용(costs)가 주어질 때 
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용?

costs[i][0], costs[i][1] => 다리가 연결되는 두 섬의 번호
costs[i][2] => 두 섬을 연결하는 다리를 건설할 때 드는 비용

모든 섬 사이의 다리 건설 비용이 주어지진 않는다.
이 경우, 두 섬 사이의 건설은 불가능 한 것

"""
from collections import deque 


cnt = 0

def solution(n, costs):
    global cnt
    # 그래프 생성
    graph = [
        []
        for _ in range(n)
    ]

    # 큐 생성
    q = deque()

    # 초기 단계
    for cost in costs :
        graph[cost[0]].append(cost[1])
        graph[cost[1]].append(cost[0])

    def bfs() :
        global cnt 
        while q :
            curr_v = q.popleft()
            cnt += 1

            for next_v in graph[curr_v] :
                if not visited[next_v] : 
                    visited[next_v] = True 
                    q.append(next_v)

    # 각 노드에서 출발했을 때 모든 노드를 지나게 되는 이동 횟수
    move_cnt = []
    cnt = 0

    for node in range(n) :
        cnt = 0

        # 방문 여부 확인 
        visited = [
            False 
            for _ in range(n)
        ]

        q.append(node)
        visited[node] = True 
        bfs()

        move_cnt.append(cnt)

    return move_cnt

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))