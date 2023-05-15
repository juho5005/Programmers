def solution(lottos, win_nums):
    ratings = {
        6 : 1,
        5 : 2, 
        4 : 3, 
        3 : 4,
        2 : 5
    }
    
    max_rating = 0
    min_rating = 0

    cnt = 0
    cnt_0 = 0
    for lotto in lottos :
        if lotto != 0 : 
            if lotto in win_nums : 
                cnt += 1
        else :
            cnt_0 += 1
    
    if (cnt+cnt_0) not in ratings :
        max_rating = 6
    else :
        max_rating = ratings[cnt+cnt_0]
    
    if cnt not in ratings :
        min_rating = 6
    else :
        min_rating = ratings[cnt]

    return [max_rating, min_rating]