from collections import deque 

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)

    flag = True 
    finish = 0
    # True => Cards1
    # False => Cards2

    is_impossible = False 

    # 원하는 글자가 남아있을 때
    while goal :

        if finish == 2 :
            is_impossible = True 
            break 

        if flag : # cards1
            while goal and cards1 and cards1[0] == goal[0] :
                cards1.popleft()
                goal.popleft()
                finish = 0
            flag = False 
            finish += 1
        
        else : # cards2
            while goal and cards2 and cards2[0] == goal[0] :
                cards2.popleft()
                goal.popleft()
                finish = 0
            flag = True
            finish += 1 

    if is_impossible : 
        return "No"
    else :
        return "Yes"