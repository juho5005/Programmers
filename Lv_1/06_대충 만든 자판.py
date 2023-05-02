def solution(keymap, targets):
    answer = []

    for target in targets :
        whole_cnt = 0
        is_impossible = False 

        for elem_target in target : 
            min_cnt = 101
            minus_cnt = 0

            for elem_keymap in keymap :
                z = elem_keymap.find(elem_target)

                if z == -1 :
                    minus_cnt += 1
                else :
                    min_cnt = min(min_cnt, z)
            
            if minus_cnt == len(keymap) :
                is_impossible = True     
                break
            
            else :
                whole_cnt += (min_cnt+1) 

        if is_impossible : 
            answer.append(-1)
            continue 
        
        answer.append(whole_cnt)

    return answer