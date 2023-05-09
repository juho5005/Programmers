def solution(t, p):
    cnt = 0
    
    maked_l = len(p)


    l = len(t) - maked_l  

    for i in range(l+1) :
        z = ''.join(t[i:i+maked_l])

        if int(z) <= int(p) :
            cnt += 1
    return cnt    