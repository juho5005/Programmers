def solution(s):
    stack = []

    for elem in s :
        if elem == '(' :
            stack.append('(')
        
        else :
            if not stack or stack[-1] != '(' :
                return False 
            stack.pop()
    
    if stack : 
        return False 
    return True 

print(solution(")()("))