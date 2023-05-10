def solution(d, budget):
    d.sort()

    sum_budget = 0 

    for idx, elem in enumerate(d) :
        sum_budget += elem 
        
        if sum_budget > budget : 
            return idx
    return len(d)