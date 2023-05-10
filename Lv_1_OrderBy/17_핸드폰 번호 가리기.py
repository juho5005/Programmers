def solution(phone_number):
    asterisk = "*" * (len(phone_number) - 4)
    
    rest_lst = phone_number[-4:]
    rest_str = "".join(rest_lst)

    return asterisk + rest_str