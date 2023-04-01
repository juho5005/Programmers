def solution(progresses, speeds):
    extra_times = []
    
    for i in range(len(progresses)) :
        if (100-progresses[i]) % speeds[i] == 0 :
            extra_times.append((100-progresses[i]) // speeds[i])
        else :
            extra_times.append( ((100-progresses[i]) // speeds[i]) + 1)

    now = 0
    cnt_lst = []

    for i in range(1, len(extra_times)) :
        if extra_times[i] > extra_times[now] : 
            cnt_lst.append(i-now)
            now = i 

    cnt_lst.append(len(extra_times) - now)
    
    return extra_times