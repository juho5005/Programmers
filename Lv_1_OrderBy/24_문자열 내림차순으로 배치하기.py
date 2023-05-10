def solution(s):
    s_lower_lst = []
    s_upper_lst = []

    for elem in s :
        if elem.islower() :
            s_lower_lst.append(elem)
        else :
            s_upper_lst.append(elem)

    s_lower_lst.sort(key=str.lower, reverse=True)
    s_upper_lst.sort(key=str.upper, reverse=True)

    return "".join(s_lower_lst) + "".join(s_upper_lst)