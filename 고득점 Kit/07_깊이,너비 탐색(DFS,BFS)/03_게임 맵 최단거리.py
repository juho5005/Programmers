# BFS
# 최단거리
from collections import deque

def solution(maps):
    # 맵의 가로, 세로 길이
    n = len(maps)
    m = len(maps[0])
    
    # 동, 서, 남, 북
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]

    # 덱 설정
    q = deque()

    # visited
    visited = [
        [False for _ in range(m)]
        for _ in range(n)
    ]

    # min-dist 
    # 지나간 칸의 개수를 세므로 시작을 1로 설정함
    dist = [
        [1 for _ in range(m)]
        for _ in range(n)
    ]
    
    def in_range(x, y) :
        return x>=0 and x<n and y>=0 and y<m 
    
    def can_go(x, y) :
        if not in_range(x, y) :
            return False 
        if visited[x][y] :
            return False 
        if maps[x][y] == 0 :
            return False 
        return True 
    
    def bfs() :
        while q :
            x, y = q.popleft()

            for dx, dy in zip(dxs, dys) :
                nx, ny = x+dx, y+dy 

                if can_go(nx, ny) :
                    visited[nx][ny] = True 
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    
    q.append((0, 0))
    visited[0][0] = True 
    bfs()

    if not visited[-1][-1] :
        return -1
    else :
        return dist[-1][-1] 