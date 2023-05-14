def solution(nums):
    l = len(nums) // 2 # 뽑아야 하는 포켓몬의 개수
    
    dic = {} # 딕셔너리 생성

    not_duplicated_nums = list(set(nums))

    res = 0 
    for elem in not_duplicated_nums :
        if l == res :
            break 

        if elem not in dic :
            dic[elem] = 0
            res += 1
        else :
            break 
    return res