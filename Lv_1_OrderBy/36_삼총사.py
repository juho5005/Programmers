def solution(number):
    l = len(number)
    cnt = 0

    for i in range(l) :
        for j in range(i+1, l) :
            for k in range(j+1, l) :
                if number[i] + number[j] + number[k] == 0 :
                    cnt += 1
    return cnt 