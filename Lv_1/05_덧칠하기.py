from collections import deque 
def solution(n, m, section):
    # 페인트칠 하는 횟수
    cnt = 0

    # popleft()를 쓰기 위해 덱으로 변환
    section = deque(section)

    while section :
        started_paint = section.popleft()
        cnt += 1

        # 칠하기로 한 벽이 페인트칠하는 롤러의 범위 내에 있을 때
        while section and (started_paint <= section[0] < started_paint + m) :
            section.popleft()

    return cnt