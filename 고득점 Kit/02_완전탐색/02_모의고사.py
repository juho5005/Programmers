first = [1,2,3,4,5] 
first *= (10000//5)

second = [2, 1, 2, 3, 2, 4, 2, 5]
second *= ((10000//8))

third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
third *= (10000//10)

def solution(answers):
    global first, second, third
    answer = []

    f_cnt = 0 # 첫 번째 사람이 맞춘 개수 
    for f, a in zip(first, answers) :
        if f == a :
            f_cnt += 1
    
    s_cnt = 0 # 두 번째 사람이 맞춘 개수 
    for s, a in zip(second, answers) :
        if s == a :
            s_cnt += 1

    t_cnt = 0 # 세 번째 사람이 맞춘 개수 
    for t, a in zip(third, answers) :
        if t == a :
            t_cnt += 1

    answer.append(f_cnt)
    answer.append(s_cnt)
    answer.append(t_cnt)

    max_ans = max(answer)
    
    if answer.count(max_ans) == 1 :
        for i, a in enumerate(answer, start=1) :
            if a == max_ans :
                return [i]
    else : 
        r = []
        for i, a in enumerate(answer, start=1) :
            if a == max_ans :
                r.append(i)
            
        r.sort() # 오름차순 정렬
        return r