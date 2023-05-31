def solution(k, tangerine):
    dic = {}

    for t in tangerine :
        if t not in dic :
            dic[t] = 1
        else :
            dic[t] += 1
    
    sorted_dic = sorted(dic.items(), key=lambda data:data[1], reverse=True)
    
    cnt = 0
    sum_of_k = 0 
    for elem in sorted_dic :
        sum_of_k += elem[1]
        cnt += 1

        if sum_of_k >= k :
            break 
    return cnt 