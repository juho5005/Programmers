def solution(wallpaper):
    row_l = len(wallpaper) # 행
    col_l = len(wallpaper[0]) # 열

    # 시작점
    start_row = 0
    start_col = 0 

    # 끝점
    finish_row = 0 
    finish_col = 0 

    # 시작점의 행 위치
    is_finish = False 
    for i in range(row_l) :
        for j in range(col_l) :
            if wallpaper[i][j] == '#' :
                start_row = i
                is_finish = True 
        if is_finish : 
            break 

    # 시작점의 열 위치
    is_finish = False 
    for i in range(col_l) :
        for j in range(row_l) :
            if wallpaper[j][i] == '#' :
                start_col = i
                is_finish = True
        if is_finish : 
            break 
    
    # 끝점의 행 위치
    is_finish = False 
    for i in range(col_l-1, -1, -1) :
        for j in range(row_l-1,-1 ,-1) :
            if wallpaper[j][i] == '#' :
                finish_col = i+1
                is_finish = True 
        if is_finish : 
            break 

    # 끝점의 열 위치
    is_finish = False 
    for i in range(row_l-1, -1, -1) :
        for j in range(col_l-1,-1 ,-1) :
            if wallpaper[i][j] == '#' :
                finish_row = i+1
                is_finish = True 
        if is_finish : 
            break 
    
    return [start_row, start_col, finish_row, finish_col]

print(solution(["..", "#."]))