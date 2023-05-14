def solution(k, score):
    res = []

    honor = []

    for idx, elem in enumerate(score, start=1) :
        if idx <= k :
            honor.append(elem)
            honor.sort()
            res.append(honor[0])
        else :
            honor.append(elem)
            honor.sort()
            honor.pop(0)

            res.append(honor[0])
    return res