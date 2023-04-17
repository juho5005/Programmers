def solution(name):

    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name) :
        # 해당 알파벳 변경 회솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next_A = i + 1

        while next_A < len(name) and name[next_A] == 'A' :
            next_A += 1

        # 기존, 연속된 A의 왼쪽 시작 방식
        # 연속된 A의 오른쪽 시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next_A, \
                        2 * (len(name) - next_A) + i])

    answer += min_move 
    return answer