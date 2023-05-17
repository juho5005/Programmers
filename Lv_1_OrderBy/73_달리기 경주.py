def solution(players, callings):
    dic = {} 
    dic1 = {}
    for idx, elem in enumerate(players, start=1) :
        dic[elem] = idx
        dic1[idx] = elem 

    for calling in callings :
        # 현재 등수
        x = dic[calling]

        # 등수가 밀린 애를 찾음
        prev_first = dic1[x-1] 

        # 등수를 높여줌
        dic[calling] = x - 1

        dic[prev_first] = x 
    
        dic1[x] = prev_first 
        dic1[x-1] = calling
    
    sorted_dic = sorted(dic.items(), key=lambda data:data[1])

    result = []
    for elem in sorted_dic :
        result.append(elem[0])
    return result