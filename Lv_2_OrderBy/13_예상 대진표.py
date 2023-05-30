'''
<인덱스를 2로 나눈 몫을 이용하기 위해 -1을 한 후 진행>
0 1 2 3 4 5 6 7 
|
0 1 2 3 
|
0 1 
|
0
'''
def solution(n,a,b):
    cnt = 0

    # 2로 나눌 때 몫을 이용하기 위해 -1을 빼준다.
    a -= 1 
    b -= 1

    while a != b :
        cnt += 1
        a //= 2 
        b //= 2
    
    return cnt 