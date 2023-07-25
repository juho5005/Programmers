'''
일정 금액을 지불하면 10일간 회원 자격

회원을 대상으로 매일 한 가지 제품을 할인하는 행사

제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수

+) 없으면 0 return 
'''

# number의 원소의 합은 10
# 10 <= len(discount) <= 100,000

def solution(want, number, discount):
    stuffs = {}
    for w, n in zip(want, number) :
        stuffs[w] = n 
    
    # discount의 길이
    l = len(discount)

    # 정답
    cnt = 0
    
    for i in range(l-10+1) :
        dic = {}
        for j in range(i, i+10) :   
            if discount[j] not in dic :
                dic[discount[j]] = 1
            else :
                dic[discount[j]] += 1

        is_true = True 
        for a, b in zip(sorted(stuffs.items()), sorted(dic.items())) :
            if a != b :
                is_true = False 
                break 
        
        if is_true : 
            cnt += 1
    
    if cnt == 0 :
        return 0 
    else :
        return cnt