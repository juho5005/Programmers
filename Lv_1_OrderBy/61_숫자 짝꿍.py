def solution(X, Y):
    x_dic = {}
    y_dic = {}

    for x in X : # O(N)
        if int(x) not in x_dic :
            x_dic[int(x)] = 1
        else :
            x_dic[int(x)] += 1
    
    for y in Y : # O(N)
        if int(y) not in y_dic :
            y_dic[int(y)] = 1
        else :
            y_dic[int(y)] += 1

    nums_lst = []
    for k in x_dic.keys() :
        if k in y_dic :
            l = min(x_dic[k], y_dic[k])
            
            for _ in range(l) :
                nums_lst.append(k)
    
    if len(nums_lst) == 0 :
        return '-1'
    
    if sum(nums_lst) == 0 :
        return '0'

    nums_lst.sort(reverse=True) # order by desc

    res = ''
    for elem in nums_lst :
        res += str(elem)
    return res