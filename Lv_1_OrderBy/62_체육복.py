def solution(n, lost, reserve):
    students = [0] * (n+1)

    # 잃어버린 학생
    for elem in lost :
        students[elem] = -1
    
    # 여분을 가진 학생
    for elem in reserve :
        students[elem] += 1
    students.pop(0)
    
    for i, student in enumerate(students) :
        if student < 0 : # 체육복을 잃어버린 경우 
            if (i-1 != -1 and students[i-1] == 1) :
                students[i-1] -= 1 
                students[i] += 1
            elif (i+1 != n and students[i+1] == 1 ) :
                students[i+1] -= 1 
                students[i] += 1
    
    cnt = 0
    for elem in students :
        if elem >= 0 :
            cnt += 1
    return cnt     