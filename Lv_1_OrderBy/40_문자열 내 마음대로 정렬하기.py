def solution(strings, n):
    strings.sort(key=lambda data:(data[n],data))
    return strings