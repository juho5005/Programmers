INT_MAX = 10000

def solution(answers):
    one = [1, 2, 3, 4, 5] * (INT_MAX // 5)
    two = [2, 1, 2, 3, 2, 4, 2, 5] * (INT_MAX // 8)
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (INT_MAX // 10)

    one_res = 0
    two_res = 0
    three_res = 0

    for i, elem in enumerate(answers) : 
        if elem == one[i] :
            one_res += 1
        if elem == two[i] : 
            two_res += 1
        if elem == three[i] :
            three_res += 1

    max_res = max(one_res, two_res, three_res) 

    res = []

    for idx, elem in enumerate([one_res, two_res, three_res], start = 1) :
        if elem == max_res :
            res.append(idx)
    return sorted(res)