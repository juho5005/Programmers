def solution(numbers):
    ans = []
    for i in range(len(numbers)) :
        for j in range(i+1, len(numbers)) :
            ans.append(numbers[i] + numbers[j])
    return sorted(list(set(ans)))