def solution(A,B):
    lst_A = sorted(A)
    lst_B = sorted(B, reverse=True)
    res = 0

    for a, b in zip(lst_A, lst_B) :
        res += a*b

    return res