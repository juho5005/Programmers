def solution(s):
    if len(s) != 4 and len(s) != 6 :
        return False 

    for elem in s :
        if 65 <= ord(elem) <= 122 :
            return False 
    return True