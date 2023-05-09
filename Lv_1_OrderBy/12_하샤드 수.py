def solution(x):
    # 자리수의 합
    jarisu= 0
    
    for elem in str(x) :
        jarisu += int(elem)

    if x % jarisu == 0 :
        return True 
    return False 