from collections import deque 

def solution(n, wires):
    
    # 그래프 생성
    graph = [
        []
        for _ in range(n+1)
    ]

    # 전선 연결
    for s, e in wires : 
        graph[s].append(e)
        graph[e].append(s)
    

    # bfs() 구현
    def bfs(root_v) :
        # 덱 생성
        q = deque()
        
        # 방문 판별
        visited = [
            False 
            for _ in range(n+1)
        ]
        
        # root_v에 대한 초기설정
        q.append(root_v)
        visited[root_v] = True 

        # 연결된 송전탑의 수 
        cnt = 1

        # bfs 실행
        while q : 
            curr_v = q.popleft()

            for next_v in graph[curr_v] :
                if not visited[next_v] : 
                    cnt += 1
                    visited[next_v] = True 
                    q.append(next_v)
        
        return cnt 
    
    # 두 쌍이 이뤄질 때 최소의 송전탑 개수의 차이
    ans = float('inf')

    # 전선상을 제거하는 모든 경우의 수 생각
    for s, e in wires : 

        # 전선 한 쌍 제거
        graph[s].remove(e)
        graph[e].remove(s)

        ans = min(ans, abs(bfs(s) - bfs(e)))

        # 전선 한 쌍 복귀
        graph[s].append(e)
        graph[e].append(s)
    
    return ans 