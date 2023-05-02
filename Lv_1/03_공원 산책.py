def solution(park, routes):
    def in_range(x, y) :
        return x >= 0 and x < len(park) and y >= 0 and y < len(park[0])

    def can_go(x, y) :
        if not in_range(x, y) :
            return False 
        if park[x][y] == 'X' :
            return False 
        return True 

    is_finish = False 
    for i in range(len(park)) :
        for j in range(len(park[0])) :
            if park[i][j] == 'S' :
                cur_x = i 
                cur_y = j
                is_finish = True 
                break 
        if is_finish :
            break 

    for route in routes :
        can_order = True  
        change_x, change_y = cur_x, cur_y 

        for i in range(int(route[2])) :
            if route[0] == 'E' :
                change_y += 1 
                if not can_go(change_x, change_y) :
                    can_order = False 
            
            elif route[0] == 'W' :
                change_y -= 1
                if not can_go(change_x, change_y) :
                    can_order = False 

            elif route[0] == 'N' :
                change_x -= 1
                if not can_go(change_x, change_y) :
                    can_order = False 

            elif route[0] == 'S' :
                change_x += 1
                if not can_go(change_x, change_y) :
                    can_order = False 

            if not can_order :
                break 
        
        if can_order : 
            cur_x, cur_y = change_x, change_y
    
    return [cur_x, cur_y]