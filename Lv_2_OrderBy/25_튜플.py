def solution(s):
    s = s[1:-1]
    new_s =s.split('},')

    l = len(new_s)
    
    members = []
    
    for idx, elem in enumerate(new_s) :    
        if idx == l-1 :
            members.append(elem[1:-1])
        else :
            members.append(elem[1:])
    
    members.sort(key=len)
    
    ans = []
    
    for member in members :
        nums = []
        nums = member.split(',')

        for num in nums :
            if int(num) not in ans :
                ans.append(int(num))
                break 
    
    return ans 