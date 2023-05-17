def solution(s, skip, index):
    res = ''

    for elem in s :
        
        idx = 0
        x = ord(elem)

        while idx < index :
            x = x + 1
            
            if x > ord('z') : # z를 넘어갈 때 
                x = ord('a')  # a로 변경

                if chr(x) in skip :
                    continue 
               
                idx += 1
                continue 
            
            if chr(x) in skip :
                continue 

            idx += 1
        
        res += chr(x)

    return res