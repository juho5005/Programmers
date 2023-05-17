def solution(ingredient):
    cnt = 0
    stack = []

    for elem in ingredient : # O(N)
        stack.append(elem) 
        
        if stack[-4:] == [1, 2, 3, 1] :
            cnt += 1

            for _ in range(4) :
                stack.pop()
    return cnt 
    
print(solution([1, 4, 3, 1, 2, 3, 1]))