from collections import defaultdict  

def solution(tickets) :
    # 가능한 모든 경로들의 집합
    answer = []

    # 기본값이 list인 딕셔너리
    dic = defaultdict(list)

    # 딕셔너리의 key : 출발지, value : 도착지
    for ticket in tickets :
        dic[ticket[0]].append(ticket[1])

    # 역순으로 도착지를 정렬
    for key in dic.keys() :
        dic[key].sort(reverse=True)


    stack = ["ICN"]

    while stack  :
        top = stack[-1] 

        if not dic[top] or len(dic[top]) == 0 :
            answer.append(stack.pop())
        else :
            stack.append(dic[top].pop())
    
    return answer[::-1]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)