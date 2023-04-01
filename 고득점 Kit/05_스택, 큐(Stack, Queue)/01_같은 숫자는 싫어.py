def solution(arr):
    stack = []

    stack.append(arr[0])

    for elem in arr[1:] :
        if stack[-1] != elem :
            stack.append(elem)
    return stack