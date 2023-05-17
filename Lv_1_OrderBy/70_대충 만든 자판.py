def solution(keymap, targets):
    alpha = {}

    for key in keymap : 
        idx = 1

        for k in key  :
            if k not in alpha : 
                alpha[k] = idx 
            else :
                if idx < alpha[k] :
                    alpha[k] = idx 
            idx += 1
    
    result = []
    for target in targets :
        res = 0
        is_finish = False

        for t in target : 
            if t not in alpha : 
                result.append(-1)
                is_finish = True                 
                break
            res += alpha[t] 
        
        if is_finish : 
            continue 
        result.append(res)
    return result
