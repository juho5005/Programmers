from itertools import permutations

k = 80
dungeons = [[80,20],[50,40],[30,10]]


def solution(k, dungeons):
    # 최대로 탐험할 수 있는 던전 개수
    max_dungeon = float('-inf')

    for elems in permutations(dungeons) :
        update_k = k

        cnt = 0 # 던전의 개수를 세어줄 변수

        for elem in elems :
            if update_k >= elem[0] :
                cnt += 1
                update_k -= elem[1]
            else :
                break 
        max_dungeon = max(max_dungeon, cnt)
    
    return max_dungeon