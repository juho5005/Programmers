def solution(s):
    def binary_divide(n) :
        nums = []
        while n != 0 :
            nums.append(n%2)
            n = n//2
        return ''.join(str(elem) for elem in reversed(nums))

    removed_zero_cnt = 0
    divide_cnt = 0

    while s != '1' :
        divide_cnt += 1
        zero_cnt = 0

        for elem in s :
            if elem == '0' :
                zero_cnt += 1
                continue 
    
        removed_zero_cnt += zero_cnt 
        l = len(s) - zero_cnt
        s = binary_divide(l)
    
    return [divide_cnt, removed_zero_cnt]