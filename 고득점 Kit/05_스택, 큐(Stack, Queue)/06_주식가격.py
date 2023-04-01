# 초 단위로 기록된 주식가격이 담긴 배열 prices 
# 가격이 떨어지지 않은 기간은 몇 초인지 return 

from collections import deque 

def solution(prices):
    # prices 리스트를 덱으로 만들어줌 
    prices_dq = deque(prices)

    # prices 덱의 길이
    l = len(prices_dq)

    # 정답 리스트
    time_lst = []

    while l != 1 :
        # 비교 대상 
        compare = prices_dq.popleft()

        time = 0

        for price in prices_dq :
            time += 1
            if price >= compare :
                continue
            else :
                break

        time_lst.append(time)
        l -= 1
        
    time_lst.append(0) # 마지막 요소는 어차피 0

    return time_lst

prices = [1, 2, 3, 2, 3]
print(solution(prices))