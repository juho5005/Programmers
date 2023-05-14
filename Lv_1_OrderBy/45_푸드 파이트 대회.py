def solution(food):
    left = ''
    middle = '0'
    right = ''

    for idx, elem in enumerate(food[1:], start=1) :
        for _ in range(elem // 2 ) :
            left += str(idx)
            right = str(idx) + right

    return left+middle+right