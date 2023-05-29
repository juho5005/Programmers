def solution(park, routes):
    row_l = len(park)
    col_l = len(park[0])

    # 맵의 범위
    def in_range(x, y) :
        return x>=0 and x<row_l and y>=0 and y<col_l 
    
    # 다음 칸을 갈 수 있는가?
    def can_go(x, y) :
        if not in_range(x, y) :
            return False 
        if park[x][y] == 'X' :
            return False 
        return True 
    
    # 초기 칸
    x, y = 0, 0 

    # 초기 칸인 'S' 찾기
    for i in range(row_l) :
        is_finish = False 
        for j in range(col_l) :
            if park[i][j] == 'S' :
                x, y = i, j
                is_finish = True 
                break 
        if is_finish :
            break 
    
    for route in routes :
        z = route.split(" ")
        z[1] = int(z[1]) # 정수 변환
        
        if z[0] == 'E' : # 동
            is_change = True 
            for i in range(1, z[1]+1) :
                if not can_go(x, y+i) :
                    is_change = False 
                    break 
            if is_change :
                x, y = x, y+z[1]
            
        elif z[0] == 'W' : # 서
            is_change = True 
            for i in range(1, z[1]+1) :
                if not can_go(x, y-i) :
                    is_change = False 
                    break 
            if is_change :
                x, y = x, y-z[1]

        elif z[0] == 'S' : # 남
            is_change = True 
            for i in range(1, z[1]+1) :
                if not can_go(x+i, y) :
                    is_change = False 
                    break 
            if is_change :
                x, y = x+z[1], y

        else : # 북
            is_change = True 
            for i in range(1, z[1]+1) :
                if not can_go(x-i, y) :
                    is_change = False 
                    break
            if is_change :
                x, y = x-z[1], y
    return [x, y]

solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]	)