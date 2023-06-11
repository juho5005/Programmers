def solution(citations):
    if sum(citations) == 0 :
        return 0

    citations.sort() # sort by desc 
    l = len(citations) # length of citations 
    max_num = citations[-1]

    while max_num :
        cnt = 0
        for i in range(l-1, -1, -1) :
            if max_num <= citations[i] :
                cnt += 1
        
        if (cnt >= max_num) and ((l-cnt) <= max_num):
            return max_num

        max_num -= 1


print(solution([0,0,0,0,0]))