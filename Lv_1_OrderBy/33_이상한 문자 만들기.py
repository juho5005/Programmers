def solution(s):
    lst = s.split(' ')
    
    changed_s = []

    for elems in lst :
        word = ''
        for idx, elem in enumerate(elems) :
            if idx % 2 == 0 :
                word += elem.upper()
            else :
                word += elem.lower()
        changed_s.append(word)
    
    res = ''
    l = len(changed_s) - 1
    for idx, elem in enumerate(changed_s) :
        res += elem 
        
        if idx == l :
            return res
        res += ' '