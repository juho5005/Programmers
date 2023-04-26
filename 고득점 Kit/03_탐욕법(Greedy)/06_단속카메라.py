def solution(routes):
    cnt = 0 # 카메라의 개수
    
    # 차량이 남아있는 경우
    while routes :
        # 고속도로에서 진출하는 시점을 기준으로 오름차순 정렬
        routes.sort(key=lambda data:data[1])

        out_pos = routes.pop(0)[1] # 진출 시점을 기준점 
        cnt += 1 # 카메라를 한 대 설치

        # 더 이상 따질 차량이 없을 때
        if not routes :
            break 

        # 진출 기준인 out_pos보다 일찍 진입한 차량들의 인덱스 모음
        out_idx_list = []
        for idx, elem in enumerate(routes) :
            if elem[0] <= out_pos  :
                out_idx_list.append(idx)
        
        # 모아놨던 인덱스를 pop 시켜줌
        for remove_idx in reversed(out_idx_list) : 
            routes.pop(remove_idx)
    
    return cnt