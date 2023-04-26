def solution(routes):
    # 카메라의 개수 
    cnt = 0 

    # 초기 카메라의 위치를 고속도로의 가장 작은 지점 -1 
    camera = -30001

    # 차량의 진출 시점을 기준으로 오름차순 정렬 
    routes.sort(key=lambda data:data[1])

    # 어떠한 진입 시점이 카메라의 설치위치보다 큰 경우 
    # 카메라의 위치를 새롭게 설치해주고 카메라의 개수를 늘려줌
    for route in routes :
        if camera < route[0] :
            cnt += 1
            camera = route[1]

    return cnt 