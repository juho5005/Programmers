def solution(t, p):
    int_p = int(p)

    l = len(t)
    p_l = len(p)

    cnt = 0
    for i in range(0, l-p_l+1) :
        if int_p >= int(t[i:i+p_l]) :
            cnt += 1
    return cnt 