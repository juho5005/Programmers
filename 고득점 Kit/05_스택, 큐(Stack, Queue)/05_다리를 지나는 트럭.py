from collections import deque 

def solution(bridge_length, weight, truck_weights):
    # 다리길이 만큼의 다리 생성 (0으로 채움)
    bridge = deque(
        0
        for _ in range(bridge_length)
    )

    # 소요 시간
    time = 0

    # 다리의 무게 
    bridge_weight = 0

    # 트럭 무게도 덱으로 만들어줌
    truck_weights_dq = deque(truck_weights)

    while truck_weights_dq :
        
        # 다리의 가장 왼쪽 pop 
        bridge_weight -= bridge.popleft()
        
        # 시간 + 1
        time  += 1

        # bridge의 무게와 새로 들어오는 트럭의 무게의 합이
        # weight 보다 작을 때만 새로 들어오는 트럭을 넣어줌
        if (bridge_weight + truck_weights_dq[0]) <= weight : 
            bridge_weight += truck_weights_dq[0]
            bridge.append(truck_weights_dq.popleft())
        
        else :
            bridge.append(0)
    
    # 마지막 트럭이 들어가자마자 while문이 종료되므로
    # 마지막 트럭이 다리를 지나는 시간만큼 더해준다
    time += bridge_length

    return time
    
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))