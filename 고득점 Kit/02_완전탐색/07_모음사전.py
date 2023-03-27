alphas = ['A', 'E', 'I', 'O', 'U']

ans = []

seq = 0

# 원하는 알파벳을 찾은 경우 다른 조건들은 차치하고 빠르게 종료
is_exit = False 

# curr_num번째 숫자를 의미
def choose(word) :
    global seq, is_exit

    if len(ans) == 5 : 
        ans.pop()
        return 

    for alp in alphas :
        # 첫 번째 종료 조건 위치
        if is_exit :
            return 
        
        ans.append(alp)
        seq += 1

        if ''.join(ans) == word : 
            is_exit = True 
            
            # 두 번째 종료 조건 위치
            if is_exit :
                return
    
        choose(word)

    ans.pop()

def solution(word):
    choose(word)
    return seq