def solution(s):
    prev = []

    res = []

    for idx, elem in enumerate(s) :
        if elem not in prev :
            prev.append(elem)
            res.append(-1)
        else :
            cnt = 1
            for i in range(idx-1, -1, -1) :
                if s[i] == elem :
                    res.append(cnt)
                    break
                cnt += 1
    return res