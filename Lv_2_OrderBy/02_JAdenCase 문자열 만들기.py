def solution(s):
    splited_s = s.split(" ")
    
    res = ''
    for i, elems in enumerate(splited_s) :
        elem_res= ''
        if elems == ' ' :
            continue 

        for idx, elem in enumerate(elems) :
            if idx == 0 :
                if elem.isalpha() :
                    elem_res += elem.upper()
                else :
                    elem_res += elem 
            else :
                if elem.isalpha() :
                    elem_res += elem.lower()
        
        if i != len(splited_s) - 1 :
            res += (elem_res + ' ')
        else :
            res += elem_res
    return res