def solution(nums):
    dic = {}

    for num in nums :
        if num not in dic :
            dic[num] = 1
        else :
            dic[num] += 1
    
    if len(nums)//2 < len(dic) :
        return len(nums)//2
    else :
        return len(dic)