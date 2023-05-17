def solution(new_id):
    # 문자열을 리스트로 치환
    new_id = list(new_id)

     # 1단계 (대문자를 소문자로 치환)
    for idx, elem in enumerate(new_id) :
        if elem.isalpha() :
            new_id[idx] = new_id[idx].lower()
        
    # 2단계 (소문자, 숫자, 빼기, 밑줄, 마침표를 제외하고 제거 )
    removed_idx = []
    for idx, elem in enumerate(new_id) :
        if (elem.isalnum() or elem == '-' or \
        elem == '_' or elem =='.') :
            continue 
        removed_idx.append(idx)
    
    for idx in reversed(removed_idx) :
        new_id.pop(idx)

    # 3단계 (마침표가 연속된 경우 한 개의 마침표로 만들어줌)
    i = 0
    l = len(new_id)
    
    new_lst = []
    while i < l : 
        if new_id[i] == '.' :
            j = i + 1 
            while j < l and new_id[j] == '.' :
                j += 1
            
            i = j
            new_lst.append('.')

        else :
            new_lst.append(new_id[i])
            i += 1

    # 4단계 ( 처음, 마지막에 위치한 '.'(마침표) 제거 )
    
    if new_lst and new_lst[0] == '.' :
        new_lst.pop(0)
    if new_lst and new_lst[-1] == '.' :
        new_lst.pop()

    # 5단계 (빈 문자열이라면 a를 대입)
    if not new_lst :
        new_lst.append('a')
    
    # 6단계 (아이디의 길이가 16자가 넘으면 첫 15개를 제외하고 다 제거)
    # 만약 제거 후 '.'가 끝에 위치한다면 그것 또한 제거

    if len(new_lst) >= 16 :
        new_lst = new_lst[:15]
    if new_lst[-1] == '.' :
        new_lst.pop()
    
    # 7단계 (길이가 2자 이하라면 마지막 문자를 길이가 3일 될 때까지 반복)
    if len(new_lst) <= 2: 
        x = new_lst[-1]
        while len(new_lst) != 3 :
            new_lst.append(x)

    return ''.join(new_lst)