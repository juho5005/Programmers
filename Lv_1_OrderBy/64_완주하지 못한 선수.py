def solution(participant, completion):
    completion_dic = {}
    participant_dic = {}

    for comp in completion :
        if comp not in completion_dic :
            completion_dic[comp] = 1
        else :
            completion_dic[comp] += 1
    
    for parti in participant :
        if parti not in participant_dic :
            participant_dic[parti] = 1 
        else :
            participant_dic[parti] += 1


    for k in participant_dic.keys() :
        if k not in completion_dic :
            return k 
    
        else :
            if participant_dic[k] > completion_dic[k] :
                return k