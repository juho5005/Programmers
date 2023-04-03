import heapq

def solution(operations):
    # create min-heap and max-heap
    min_heap, max_heap = [], []
    q = []

    # 큐의 원소 개수
    cnt = 0

    for operation in operations :
        order, num = operation.split(' ')
        num = int(num)

        if order == 'I' :
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            q.append(num)
            cnt += 1

        elif order == 'D' :
            # if queue not exists
            if cnt == 0 :
                continue 

            if num == 1 : 
                cnt -= 1
                
                max_elem = -heapq.heappop(max_heap)
                min_heap.remove(max_elem)
                q.remove(max_elem)
                
            elif num == -1 :
                cnt -= 1
                min_elem = heapq.heappop(min_heap)
                max_heap.remove(-min_elem)
                q.remove(min_elem)

    if not q :
        return [0, 0]
    else :
        return [max(q), min(q)]