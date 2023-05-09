def solution(n):
    lst = []
    
    for elem in str(n) :
        lst.append(int(elem))
    
    lst.sort(reverse=True)

    return int(''.join(str(x) for x in lst))

print(solution(118372))