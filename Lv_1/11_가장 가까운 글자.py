'''
1 <= len(s) <= 10,000
    s는 영어 소문자로만 이루어져있음
'''

def solution(s):
    result = [-1] * len(s)
    
    prev_stack = []

    for i,elem in enumerate(s) :
        
        if elem not in prev_stack : 
            prev_stack.append(elem)
            continue  
        
        idx = -1 
        cnt = 1

        while prev_stack[idx] != elem :
            idx -= 1
            cnt += 1
        
        result[i] = cnt 
        
        prev_stack.append(elem)
    
    return result
        
s = "foobar"
print(solution(s))