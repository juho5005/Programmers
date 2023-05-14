def solution(array, commands):
    ans = []
    for command in commands :
        new_array = []

        for i in range(command[0]-1, command[1]) :
            new_array.append(array[i])

        new_array.sort()
        ans.append(new_array[command[2]-1])
    return ans 