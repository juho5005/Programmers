def solution(arr, divisor):
    ans = []

    for elem in arr :
        if elem % divisor == 0 :
            ans.append(elem)
    
    if len(ans) > 0 :
        return sorted(ans)

    return [-1]