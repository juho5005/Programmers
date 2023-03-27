def solution(participant, completion):
    dic_participant = {}

    names = []

    for elem in participant :
        if elem not in dic_participant :
            dic_participant[elem] = 1
        else :
            dic_participant[elem] += 1
    
    for comp in completion : 
        if dic_participant[comp] >= 1 : 
            dic_participant[comp] -= 1 
    
    for k, v in dic_participant.items() :
        if v >= 1 :
            names.append(k)
    
    return "".join(names)