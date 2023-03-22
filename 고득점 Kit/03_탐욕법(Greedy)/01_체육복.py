# 학생들의 번호는 체격순 
# 바로 앞 번호의 학생 or 바로 뒷 번호의 학생 에게만 빌려줄 수 있음
# 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 함

# 전체 학생의 수 : n
# 도난당한 학생들의 번호가 담긴 배열 : lost 
# 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 : reserve

# 체육 수업을 들을 수 있는 학생의 최댓값을 return 

n = 3  # 2명 이상 30명 이하
lost = [1] # 1명 이상 n명 이하, 중복 x
reserve = [3] # 1명 이상 n명 이하, 중복 x

# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있음 
# 이때 이 학생은 체육복을 하나만 도난당했다고 가정
# 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 있음

def solution(n, lost, reserve):
    
    # 0~n+1번까지 1개씩 체육복을 가지고 있다고 가정
    # 0번 배열은 사용 x
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


    

print(solution(n, lost, reserve))