def solution(a, b):
    # 2016년 1월 1일은 '금요일'
    days_of_week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    days_of_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 윤년의 2월은 29일이다.

    # 2016년 1월 1일부터 2016년 a월 b일까지의 날짜를 더함
    # 더하고 일주일인 7로 나눠줌
    # 나눠준 인덱스가 0~6까지 존재하며 0이 금요일, 6이 목요일

    # a월 이전까지의 모든 일 수를 더해줌 + b일 -1 (금요일의 인덱스가 0이기 때문이다)
    whole_days = sum(days_of_month[0:a-1]) + b - 1

    return days_of_week[whole_days%7]