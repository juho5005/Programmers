def solution(n, words):
    # 각 사용자의 번호 : 1 ~ n 
    stack = [] 
    is_fail = False 
    seq = -1

    for idx, word in enumerate(words) :
        # 단어의 길이가 1일 때 
        # 앞 사람의 마지막 단어와 새로 나오는 단어가 다를 때 
        # 이미 말했던 단어를 또 말할 때
        if len(word) == 1 or (stack and stack[-1][-1] != word[0]) \
             or word in stack :
            is_fail = True 
            seq = idx
            break
        stack.append(word)

    if not is_fail :
        return [0,0]
    else :
        # 탈락자의 번호
        a = (seq % n) + 1
        
        # 탈락자의 자기 순서
        b = (seq // n) + 1
        return [a,b]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))