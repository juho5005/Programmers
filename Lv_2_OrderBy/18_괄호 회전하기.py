def solution(s):
    l = len(s) # 문자열 s의 길이
    cnt = 0
 
    # 올바른 괄호의 배치인지 체크
    def check(a) :
        stack = []
        for elem in a :
            if (elem == '[') or (elem == '(') or (elem == '{') :
                stack.append(elem)
            else :
                if elem == ']' :
                    if not stack or stack[-1] != '[' :
                        return False 
                    stack.pop()

                elif elem == ')' :
                    if not stack or stack[-1] != '(' :
                        return False 
                    stack.pop()
                
                elif elem == '}' :
                    if not stack or stack[-1] != '{' :
                        return False 
                    stack.pop()
        if stack : 
            return False 
        return True 

    # 회전시키지 않은 경우부터 체크
    if check(s) : 
        cnt += 1
            
    while l-1 : 
        s = s[1:] + s[0]
        if check(s) :
            cnt += 1
        l -= 1 
    return cnt 