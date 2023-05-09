def solution(s):
    # 모두 대문자로 변환
    s = s.lower()

    Y_cnt = 0
    P_cnt = 0

    for elem in s :
        if elem == 'y' :
            Y_cnt += 1
            continue 
        if elem == 'p' :
            P_cnt += 1
            continue 
    
    if Y_cnt == 0 and P_cnt ==0 :
        return True 
    
    if Y_cnt == P_cnt :
        return True 
    else :
        return False 