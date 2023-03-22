import math

def aliquot(num) :
    pairs = []
    
    for i in range(1, int(math.sqrt(num)) + 1) :
        if num % i == 0 :
            pairs.append((i, num//i))
    
    return pairs
    
def solution(brown, yellow):

    # 약수 쌍들의 리스트
    pair_lst = aliquot(yellow)

    for pair in pair_lst :
        width = pair[1] + 2
        height = pair[0] + 2

        if brown == (width*2) + (height*2) - 4 :
            break 

    return [width, height]