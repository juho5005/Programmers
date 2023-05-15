def solution(dartResult):
    bonus_str = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }
    option_str = ['*', '#']

    splited_dart = []
    res = []

    i = 0
    l = len(dartResult)
    
    while i < l :
        is_plus = False 
        if dartResult[i] in bonus_str : 
            
            # 숫자 10인 경우, 문자열 10으로 만들어줌
            if len(res) == 2 :
                res = [res[0] + res[1]]
            
            res.append(dartResult[i])
            
            if not i+1 == l and dartResult[i+1] in option_str :
                res.append(dartResult[i+1])
                is_plus = True 

            splited_dart.append(res)

            if is_plus : 
                i += 2
            else :
                i += 1   
            res = []

        else :       
            res.append(dartResult[i])
            i += 1

    whole_score = 0
    scores = []
    for idx, dart in enumerate(splited_dart) :
        if len(dart) == 3 : # 옵션이 있을 때 

            if idx == 0 : # 옵션이 첫 번째로 나올 때
                if dart[2] == '*' : # '*'일 때
                    scores.append((int(dart[0]) ** bonus_str[dart[1]]) * 2)
                else : # '#'일 때
                    scores.append((int(dart[0]) ** bonus_str[dart[1]]) * -1)
            
            else : # 옵션이 뒤에서 나와서 앞에 영향을 미칠 때
                if dart[2] == '*' : # '*'일 때
                    scores[-1] = scores[-1] * 2
                    scores.append((int(dart[0]) ** bonus_str[dart[1]]) * 2)
                else : # '#'일 때
                    scores.append((int(dart[0]) ** bonus_str[dart[1]]) * -1)
        else : # 옵션이 없을 때
            scores.append((int(dart[0]) ** bonus_str[dart[1]]))

    whole_score = sum(scores)
    return whole_score