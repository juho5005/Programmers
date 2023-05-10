def solution(arr) : 
    stack = []
    stack.append(arr[0])

    for elem in arr[1:] :
        if elem != stack[-1] :
            stack.append(elem)
    return stack 