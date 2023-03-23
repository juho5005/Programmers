def solution(number, k):
    # 숫자를 담을 stack 생성 
    stack = []

    for num in number :
        # stack이 비어있는 경우 우선적으로 num을 하나 넣어준다.
        if not stack : 
            stack.append(num)
            continue 
        
        # 1) stack에 값이 존재하고
        # 2) stack[-1] 보다 num이 더 커야 하고
        # 3) 지워줘야할 개수인 k가 0보다 커야함
        while stack and stack[-1] < num and k > 0 :
            stack.pop()
            k -= 1
        stack.append(num)
        
    # 지워줘야할 개수만큼 지우지 못한 경우
    if k > 0 :
        stack = stack[:-k]
    
    return ''.join(stack)