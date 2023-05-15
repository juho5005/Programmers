from collections import deque 
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)    
    goal = deque(goal)

    # True : cards1
    # False : cards2
    flag = True
    spin = 0

    while goal : 
        if spin == 2 :
            return "No"

        if flag : # cards1
            spin += 1 
            while goal and cards1 :
                if cards1[0] == goal[0] :
                    cards1.popleft()
                    goal.popleft()
                    spin = 0 
                else :
                    break 
            flag = False 

        else : # cards2
            spin += 1 
            while goal and cards2 : 
                if cards2[0] == goal[0] :
                    cards2.popleft()
                    goal.popleft()
                    spin = 0
                else :
                    break
            flag = True 
    return "Yes"