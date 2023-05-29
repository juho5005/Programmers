def solution(n):
    cnt = 1 # 자기자신을 미리 세어줌

    for i in range(1, (n//2)+1) :
        
        sum_nums = i
        interval = 1

        while 1 :
            
            plus = (i + interval)
            interval += 1

            sum_nums += plus
            
            if sum_nums > n :
                break 
            if sum_nums == n :
                cnt += 1
                break 
    return cnt 
