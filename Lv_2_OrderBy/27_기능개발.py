def solution(progresses, speeds):
    # 각 기능의 남은 작업 일 모음
    rest_days = []
    
    for progress in progresses :
        rest_days.append(100-progress)

    spend_days = []
    
    for rest, spend in zip(rest_days, speeds) :
        if rest % spend == 0 :
            spend_days.append(rest//spend)
        else :
            spend_days.append((rest//spend) + 1)
    
    # 길이
    l = len(spend_days)

    ans = []
    std = spend_days[0]

    interval = 1

    for i in range(1, l) :
        if std >= spend_days[i] :
            interval += 1
        
        else : 
            ans.append(interval)
            interval = 1
            std = spend_days[i]
    ans.append(interval)

    return ans        