def solution(name, yearning, photo):
    dic = {}
    
    for n, y in zip(name, yearning) :
        dic[n] = y
    
    result = []
    for elems in photo :
        score = 0
        
        for elem in elems :
            if elem in dic :
                score += dic[elem]
        
        result.append(score)
    
    return result