def solution(a, b):
    res = 0

    for n1, n2 in zip(a, b) :
        res += (n1*n2)
    return res