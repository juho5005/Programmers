def solution(arr1, arr2) :
    res = []
    for elems_1, elems_2 in zip(arr1, arr2) :
        res_sub = []
        for elem_1, elem_2 in zip(elems_1, elems_2) :
            res_sub.append(elem_1 + elem_2)
        res.append(res_sub)
    return res