# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꿔서 return 

numbers = [6, 10, 2]

numbers = list(map(str, numbers))
print(numbers)

numbers.sort(key=lambda x : x*3)

print(numbers)