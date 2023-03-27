# H-Index : 생산성과 영향력을 나타내는 지표
# H-Index를 나타내는 값인 h를 구하려고 함

# 논문 n편 중 h번 이상 인용된 논문이 h편 이상이고
 # 나머지 논문이 h번 이하 인용됐다면 h의 최댓값이 이 과학자의 H-Index 

# 논문의 인용 횟수 (0 <= elem <= 10,000)
citations = [3, 0, 6, 1, 5]

# 논문의 수는 1편이상 1,000편 이하 

def solution(citations):
    n = len(citations) # 논문의 수 
    
    # h값은 n편부터 빼가면 됨
    
    res  = 0 # 답
    
    for i in range(n, 0, -1) :
        
        cnt = 0 # h번 이상 인용된 논문의 수 

        for elem in citations :
            if elem >= i  :
                cnt += 1
        
        if cnt >= i :
            res = i 
            break 

    return res

print(solution(citations))