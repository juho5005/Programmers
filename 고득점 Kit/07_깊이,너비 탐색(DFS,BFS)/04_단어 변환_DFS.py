# dfs 
import sys 
sys.setrecursionlimit(10**6)

# 최소 ans를 찾으려고 함
ans = float('inf')

# 단어의 요소의 차이의 개수를 반환하는 함수
# 즉 단어중 한 개의 문자만 다른 경우를 찾는 것
def words_diff(a, b) :
    cnt = 0

    for elem1, elem2 in zip(a, b) :
        if elem1 != elem2 :
            cnt += 1

    return cnt

def dfs(changed_cnt, curr_word, target, words) :
    global ans
    if curr_word == target :
        ans = min(ans, changed_cnt)
        return 
    
    for word in words :
        if words_diff(curr_word, word) == 1 :
            words.remove(word)
            dfs(changed_cnt+1, word, target, words)
            words.append(word)

def solution(begin, target, words):
    global ans 
    # target이 words 안에 없어서 변환할 수 없는 경우
    if target not in words :
        return 0
    
    # dfs 실행
    dfs(0, begin, target, words)
    
    # dfs를 다 돌았는데 target을 발견하지 못한 경우
    if ans == float('inf') :
        return 0
    return ans 