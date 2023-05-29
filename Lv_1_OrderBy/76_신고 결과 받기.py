def solution(id_list, report, k):
    id_dic = {} # 신고한 애들을 담아줄 거
    id_accused = {} # 신고 받은거 담아줄 거
    
    for id in id_list :
        id_dic[id] = {}
        id_accused[id] = 0

    for elem in report :
        x = elem.split(" ")

        if x[1] not in id_dic[x[0]] : # 신고한거 넣어줌
            id_dic[x[0]][x[1]] = 1

            # 신고 받으면 횟수를 늘려줌 
            id_accused[x[1]] += 1

    stop_user = []
    for key, value in id_accused.items() :
        if  value >= k :
            stop_user.append(key)
    
    # 답
    result = []

    for id in id_list :
        cnt = 0 
        for z in id_dic[id].keys() :
            if z in stop_user :
               cnt += 1
        result.append(cnt)
    return result 

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))