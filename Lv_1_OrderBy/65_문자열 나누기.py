def solution(s):
    i = 0
    l = len(s)

    cnt = 0

    while i < l :
        x = s[i]
        j = i+1 
        x_cnt = 1 
        other_cnt = 0

        is_loop = True 
        while j < l :
            
            if x != s[j] :
                other_cnt += 1 
            else :
                x_cnt += 1
            
            if x_cnt == other_cnt :
                cnt += 1
                i = j+1 
                is_loop = False 
                break
            j += 1

        if is_loop : 
            cnt += 1
            break 
    
    return cnt 

print(solution("abcc"))