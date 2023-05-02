def solution(s, skip, index) :
    ans = ''

    for elem in s : 
        start = ord(elem)

        cnt = index 

        while cnt :
            start += 1            

            # z를 넘은 경우
            if start > 122 : 
                start = 97
            
            # 스킵해야 하는 단어 목록에 있는 경우
            if chr(start) in skip :
                continue 
            
            # 스킵하지 않아도 되는 경우
            cnt -= 1 

        ans += chr(start)

    return ans 