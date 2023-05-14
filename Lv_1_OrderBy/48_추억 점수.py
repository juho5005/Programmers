def solution(name, yearning, photo):
    name_with_yearning = {}
    
    for n, y in zip(name, yearning) :
        if n not in name_with_yearning :
            name_with_yearning[n] = y 
        
    ans = []

    for p in photo : 
        res = 0

        for elem in p :
            if elem not in name_with_yearning :
                continue 
            res += name_with_yearning[elem]
        
        ans.append(res)
    return ans 