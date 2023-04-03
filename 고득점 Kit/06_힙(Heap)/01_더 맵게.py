import heapq 

def solution(scoville, K):
    mixed_cnt = 0

    # min-heap 사용
    heap_scoville = []

    for elem in scoville :
        heapq.heappush(heap_scoville, elem)

    while 1 :
        if all(K <= elem for elem in heap_scoville) :
            break 

        mixed_cnt += 1

        if len(heap_scoville) == 1 : 
            return -1
        
        a = heapq.heappop(heap_scoville)
        b = heapq.heappop(heap_scoville)

        heapq.heappush(heap_scoville, a + (b * 2)) 
        
    return mixed_cnt