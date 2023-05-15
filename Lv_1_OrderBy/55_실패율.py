def solution(N, stages):
    l = len(stages)
    max_l = l

    probability_stage = []

    for i in range(1, N+2) :
        cnt = 0

        for elem in stages :
            if elem == i :
                cnt += 1
        
        if cnt == 0 :
            probability_stage.append((i, 0))
            continue 

        if cnt == max_l : 
            probability_stage.append((i, 1))
            continue    

        try :
            probability_stage.append((i, (cnt/l)))
            l -= cnt 
        except : 
            l -= cnt
            break
    
    if probability_stage[-1][0] == N+1 :
        probability_stage.pop()

    probability_stage.sort(key=lambda data:(-data[1], data[0]))

    res = []
    for elem in probability_stage : 
        res.append(elem[0])
    return res