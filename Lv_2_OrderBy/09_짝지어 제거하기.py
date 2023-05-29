def solution(s) : 
    stack = []

    for elem in s :
        if stack and stack[-1] == elem :
            stack.pop()
            continue 
        stack.append(elem)
    
    if stack :
        return 0
    else :
        return 1