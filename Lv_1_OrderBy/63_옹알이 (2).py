def solution(babbling):
    can_speak = ["aya", "ye", "woo", "ma"]
    cnt = 0

    for babb in babbling :
        for i, speak in enumerate(can_speak) :
            if speak in babb : 
                babb = babb.replace(speak, str(i))
   
        if babb.isnumeric() :
            connectivity = False 
            for i in range(1, len(babb)) :
                if babb[i-1] == babb[i] :
                    connectivity = True 
                    break 

            if not connectivity :
                cnt += 1
    return cnt 


print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))