from collections import deque 

def solution(n, m, section):
    # 페인트를 칠하는 횟수
    cnt = 0

    # 덱으로 바꿔줌
    section = deque(section)

    while section : 
        started_point = section.popleft()
        cnt += 1

        # 칠하기로 한 벽이 페인트칠하는 롤러의 범위 내에 있을 때
        while section and (started_point <= section[0] < started_point + m) :
            section.popleft()

    return cnt     