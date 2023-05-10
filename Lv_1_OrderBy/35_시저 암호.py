def solution(s, n):
    res = ''

    for elem in s :
        if elem == " " :
            res += elem 
            continue

        if elem.isupper() :
            x = ord(elem) + n
            if x > ord('Z') :
                res += chr(ord('A') + (x - ord('Z')) - 1)
            else :
                res += chr(x)
        else : 
            x = ord(elem) + n
            if x > ord('z') :
                res += chr(ord('a') + (x - ord('z')) - 1)
            else :
                res += chr(x)
    return res