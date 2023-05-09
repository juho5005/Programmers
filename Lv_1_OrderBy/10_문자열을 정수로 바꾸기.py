def solution(s):
    if s[0] == '-' :
        num_s = int(s[1:])
        return -1 * num_s 
    return int(s[:])