def solution(arr1, arr2):
    a_lst = []
    for i in range(len(arr1)) :
        a = [elem for elem in arr1[i]]
        a_lst.append(a)


    b_lst = []
    for k in range(len(arr2[0])) :
        b = []
        for l in range(len(arr2)) :
            b.append(arr2[l][k])
        b_lst.append(b)

    ans = []

    for i in range(len(a_lst)) :
        interval = []
        for j in range(len(b_lst)) :
            res = 0 
            for q, w in zip(a_lst[i], b_lst[j]) :
                res += (q*w)
            interval.append(res)
        ans.append(interval)    
    return ans