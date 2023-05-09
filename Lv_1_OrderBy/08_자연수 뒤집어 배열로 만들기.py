def solution(n):
    ans = []

    for elem in str(n)[::-1] :
        ans.append(int(elem))

    return ans 