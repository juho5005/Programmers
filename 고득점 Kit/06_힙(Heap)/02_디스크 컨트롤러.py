import heapq 

def solution(jobs):
    # 진행한 작업의 개수
    completed_job = 0

    # 현재 시점
    now = 0

    # 이전 작업의 시작 시점 
    start = -1 # -1로 초기화 해둔다.

    # 소요된 시간
    consumed_time = 0

    # min-heap 생성
    min_heap_job = []

    # 모든 작업이 완료될 시 종료
    while completed_job < len(jobs) :
        for req_time, taked_time in jobs :
            if start < req_time <= now :
                heapq.heappush(min_heap_job, ((taked_time, req_time)))
        
        # 할 작업이 있을 때 
        if min_heap_job : 
            taked, req  = heapq.heappop(min_heap_job) # 소요시간이 가장 적은 작업을 빼줌

            start = now # 지금 진행하려는 작업이 이전 작업이 되므로 start를 now로 업데이트 
            now += taked # 소요시간만큼 현재시간에서 더해줌
            consumed_time += (now-req) # (작업이 끝난 시점 - 처음 요청이 된 시점)
            
            completed_job += 1 # 완료한 작업의 수를 더해줌
        
        # 할 작업이 없을 때
        else :
            now += 1
    
    return consumed_time // len(jobs)