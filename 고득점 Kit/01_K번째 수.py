def solution(array, commands):
    answer = []

    for command in commands :
        i,j,k = command[0], command[1], command[2]

        new_lst = array[i-1:j]
        new_lst.sort() 
        
        answer.append(new_lst[k-1])
        
    return answer