def solution(n, arr1, arr2):
    def find_binary_num(x) :
        binary_num = ''
        while x != 0 :
            binary_num = str(x%2) + binary_num
            x //= 2 
        
        if len(binary_num) != n :
            plus_zero = '0' * (n-len(binary_num))
            binary_num = plus_zero + binary_num 
        return binary_num
    
    arr1_binary = []
    arr2_binary = []
    for elem1, elem2 in zip(arr1, arr2) :
        arr1_binary.append(find_binary_num(elem1))
        arr2_binary.append(find_binary_num(elem2))
    
    res = []
    for k1, k2 in zip(arr1_binary, arr2_binary) :
        res_sub = ''
        for l1, l2 in zip(k1, k2) :
            if l1 == '1' or l2 == '1' :
                res_sub += '#'
            else :
                res_sub += ' '
        res.append(res_sub)
    return res