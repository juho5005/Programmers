changes = {
    'zero' : '0',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}

def solution(s):
    cur_idx = 0
    l = len(s) # 문자열의 총 길이

    res = '' # 일단 문자열로 받은 후 정수형으로 변환

    while cur_idx < l : 
        if ord('0') <= ord(s[cur_idx]) <= ord('9') :
            res += s[cur_idx]
            cur_idx += 1
        else : # 숫자가 아닌 경우
            temporary_s = s[cur_idx]
            cur_idx += 1

            while cur_idx < l and not (ord('0') <= ord(s[cur_idx]) <= ord('9')) :
                temporary_s += s[cur_idx]
                cur_idx += 1

                if temporary_s in changes :
                    break 
            res += changes[temporary_s]
            
    return int(res)