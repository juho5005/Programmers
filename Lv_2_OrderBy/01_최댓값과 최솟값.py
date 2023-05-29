def solution(s):
    str_nums = s.split(" ")

    int_nums = []

    for elem in str_nums :
        int_nums.append(int(elem))
    
    int_nums.sort() # order by asc
    
    max_num = str(int_nums[-1])
    min_num = str(int_nums[0])

    res = min_num + ' ' + max_num 
    
    return res