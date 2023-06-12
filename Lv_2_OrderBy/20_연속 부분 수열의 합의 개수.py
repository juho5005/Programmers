def solution(elements):
    # 결과 모음
    ress = []    

    # elements의 자릿수
    l = len(elements)
    
    for i in range(1, l+1) :
        
        k = 0 

        while k < l : 
            if (k+i-1) >= l :
                rest = (k+i-1)-l
                res = elements[k:] + elements[:rest+1]
                ress.append(sum(res))
                k += 1
            else :
                res = elements[k:k+i] 
                ress.append(sum(res))
                k += 1
        
    return len(set(ress))