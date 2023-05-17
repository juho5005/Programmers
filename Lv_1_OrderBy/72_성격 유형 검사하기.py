def solution(survey, choices):
    types_dic = {
        1 : {'R' : 0, 'T' : 0},
        2 : {'C' : 0, 'F' : 0},
        3 : {'J' : 0, 'M' : 0},
        4 : {'A' : 0, 'N' : 0}
    }
    
    one_index = ['R', 'T']
    two_index = ['C', 'F']
    three_index = ['J', 'M']

    scores = {
        1 : 3, 
        2 : 2,
        3 : 1,
        4 : 0,
        5 : 1,
        6 : 2, 
        7 : 3
    }

    for s, c in zip(survey, choices) :
        if c == 4 :
            continue 

        if s[0] in one_index : 
           type = 1 
        elif s[0] in two_index : 
            type = 2
        elif s[0] in three_index :
            type = 3 
        else :
            type = 4

        if c <= 3 :
            types_dic[type][s[0]] += scores[c]
        else :
            types_dic[type][s[1]] += scores[c]
    
    res = ''
    lst = []
    for value in types_dic.values() :
        for k, v in value.items() :
            lst.append([k, v])

    for i in range(0,len(lst), 2) :
        if lst[i][1] >= lst[i+1][1] :
            res += lst[i][0]
        else :
            res += lst[i+1][0]
    return res