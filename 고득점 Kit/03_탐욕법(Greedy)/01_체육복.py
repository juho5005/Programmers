def solution(n, lost, reserve):
    # 0~n+1번까지 1개씩 체육복을 가지고 있다고 가정
    # 0번 배열, n+1번 배열은 사용 x
    students = [
        1
        for i in range(n+2)
    ]

    # 도난당한 학생들의 체육복 수를 하나 뺀다.
    for elem1 in lost : 
        students[elem1] -= 1 
    
    # 여유 있는 학생들의 체육복 수를 하나 더한다.
    for elem2 in reserve :
        students[elem2] += 1
    
    # 도난이 이뤄지고 난 체육복을 1개이상 가진 학생의 수 
    initial_cnt = 0
    for i in range(1, n+1) :
        if students[i] >= 1 : 
            initial_cnt += 1

    # 체육복을 빌려 추가될 학생
    add_cnt = 0 
        
    for i in range(1, n+1) :
        if students[i] == 2 : 
            if students[i-1] == 0 :
                students[i-1] += 1
                add_cnt += 1 
            elif students[i+1] == 0 :
                students[i+1] += 1
                add_cnt += 1
            else :
                pass 
    
    return add_cnt + initial_cnt