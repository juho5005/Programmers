def solution(n, left, right):
    dic = {}

    idx = 0
    for i in range(1, n+1) :
        dic[idx] = i
        idx += 1
    
    ans = []
    for k in range(left, right+1) :
        l_q = k//n
        l_r = k%n
        l_ans = 0

        if l_q == 0 :
            l_ans = dic[l_r]
        elif l_q == n-1 :
            l_ans = n 
        else :
            std = dic[0] + l_q
            if std >= dic[l_r] :
                l_ans = std 
            else :
                l_ans = dic[l_r]
        ans.append(l_ans)
    return ans
