def solution(board, moves):
    box = []
    disappeared_doll = 0

    row_l = len(board) # 행의 위치
    column_l = len(board[0]) # 열의 길이
    
    for m in moves : # 크레인의 위치 
        for i in range(row_l) :
            if board[i][m-1] != 0 :
                box.append(board[i][m-1])
                board[i][m-1] = 0
                break
        
        if box : 
            remove_lst = []

            box_l = len(box)

            for i in range(1, box_l) :
                if box[i-1] == box[i] :
                    remove_lst.append(i-1)
                    remove_lst.append(i)
                    disappeared_doll += 2

            for elem in reversed(remove_lst) :
                box.pop(elem)

    return disappeared_doll