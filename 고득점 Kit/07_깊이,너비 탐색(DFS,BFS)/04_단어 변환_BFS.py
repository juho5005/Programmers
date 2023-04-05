# bfs
from collections import deque 

def words_diff(a, b) :
    cnt = 0

    for elem1, elem2 in zip(a, b) :
        if elem1 != elem2 :
            cnt += 1

    return cnt

def solution(begin, target, words):

    # target이 words 안에 없어서 변환할 수 없는 경우
    if target not in words :
        return 0
    
    # 큐 생성
    q = deque()

    # 큐에 (시작 단어, 깊이)를 넣어줌
    q.append([begin, 0])

    while q :
        x, cnt = q.popleft()

        if x == target :
            return cnt # target 값이 되면 cnt 출력

        for word in words :
            if words_diff(x, word) == 1 :
                q.append([word, cnt+1])

    return 0 # target 값이 있으나 변환될 수 없는 경우 