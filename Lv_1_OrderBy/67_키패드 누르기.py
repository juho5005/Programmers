def solution(numbers, hand):
    keypad = {
        1 : (0, 0), 2 : (0, 1), 3 : (0, 2),
        4 : (1, 0), 5 : (1, 1), 6 : (1, 2),
        7 : (2, 0), 8 : (2, 1), 9 : (2, 2),
        '*' : (3, 0), 0 : (3, 1), '#' : (3, 2)
    }

    left_nums = [1, 4, 7]
    right_nums = [3, 6, 9]

    cur_left = '*'
    cur_right = '#'

    # 결과값
    res = ''
    
    for number in numbers : 
        if number in left_nums : # 왼쪽 손으로만 누를 수 있을 때
            cur_left = number 
            res += 'L' 
            continue

        elif number in right_nums : # 오른쪽 손으로만 누를 수 있을 때
            cur_right = number 
            res += 'R'
            continue
        
        else : # 숫자가 중앙에 위치할 때

            # 왼쪽 손가락을 기준으로 원하는 숫자와의 거리
            left_dist = abs(keypad[cur_left][0] - keypad[number][0]) + \
                        abs(keypad[cur_left][1] - keypad[number][1])
            
						# 오른쪽 손가락을 기준으로 원하는 숫자와의 거리
            right_dist = abs(keypad[cur_right][0] - keypad[number][0]) + \
                        abs(keypad[cur_right][1] - keypad[number][1])

            if left_dist > right_dist : # 오른쪽 손가락으로 누르는 거리가 더 가까운 경우
                cur_right = number 
                res += 'R'
            elif left_dist < right_dist : # 왼쪽 손가락으로 누르는 거리가 더 가까운 경우
                cur_left = number
                res += 'L'
            else : # 거리가 같은 경우 
                if hand == 'right' :
                    cur_right = number 
                    res += 'R'
                else :
                    cur_left = number
                    res += 'L'
    return res