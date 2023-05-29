def solution(today, terms, privacies):
    # 오늘 날짜 (년/월/일)
    today_lst = today.split('.')
    t_y, t_m, t_d = int(today_lst[0]), int(today_lst[1]), int(today_lst[2])
    
    # 오늘 날짜에 대한 모든 일을 더해줌 (년도는 2020부터 시작하므로 이를 기준으로 삼음)
    y = t_y - 2020
    today_sum_days = (y * 12 * 28) + (t_m * 28) + (t_d)
    
    
    # 개인정보 약관의 종류에 따른 유효기간을 딕셔너리에 저장
    term_dic = {}

    for term in terms :
        x = term.split(" ")
        term_dic[x[0]] = int(x[1])

    # 결과를 저장할 리스트
    res = []

    # 수집된 개인정보의 정보를 하나하나씩 분석
    for idx, privacy in enumerate(privacies, start=1) :
        x = privacy.split(' ')
    
        privacy_day = x[0]
        privacy_term = x[1]

        year, month, day = privacy_day.split(".")
        year, month, day = int(year), int(month), int(day)
        
        # 현재 까지의 모든 일들의 합 (년도는 2020년을 기준으로 함)
        y = year - 2020
        p_sum_days = (y * 12 * 28) + (month * 28) + (day)

        # 유효기간에 해당되는 날짜만큼 추가로 더 해줌
        p_sum_days += (term_dic[privacy_term] * 28)

        # 오늘 날짜가 유효기간을 더한 날짜보다 같거나 크다면 유효기간이 지난것이므로
        # 파기해야하는 정보들이다. (정답)
        if p_sum_days <= today_sum_days :
            res.append(idx)
    return res