def solution(numbers):
    nums = [
        i
        for i in range(10)
    ]

    for elem in numbers :
        if elem in nums :
            nums.remove(elem)
    return sum(nums)