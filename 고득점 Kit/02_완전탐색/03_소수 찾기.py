import math 
from itertools import permutations

# 최대 숫자 (7자)
INT_MAX = 9876543

nums = [
    True 
    for i in range(INT_MAX+1)
]

# 0과 1은 소수가 아니다
nums[0], nums[1] = False, False 

# 에라토스테네스의 체 사용
for i in range(2, int(math.sqrt(INT_MAX))+1) :
    if nums[i] : 
        j = 2
        while i*j <= INT_MAX :
            nums[i*j] = False 
            j += 1

def solution(numbers):
    answer = 0
    elements = []

    for n in numbers :
        elements.append(n)

    # 만들수 있는 최대 자리수
    max_jarisu = len(numbers)

    # 만들 수 있는 수들
    maked_nums = []

    for i in range(1, max_jarisu + 1) :

        for elem in permutations(elements, i) :
            maked_nums.append(int(''.join(elem)))

    maked_nums = set(maked_nums)

    for num in maked_nums :
        if nums[num] : 
            answer += 1
    return answer