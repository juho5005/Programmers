def solution(players, callings):
    # 선수들의 이름과 그 당시 인덱스를
    # (key, value)로 저장해두기
    dic = {}

    for idx, player in enumerate(players) :
        dic[player] = idx 
    
    for calling in callings : 
        pos = dic[calling]

        dic[players[pos]] = pos-1 
        dic[players[pos-1]] = pos

        players[pos-1], players[pos] = players[pos], players[pos-1]

    return players