"""
고속도로를 이용하는 차량의 경로 routes 
모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 
최소 몇 대의 카메라의 설치가 필요한가?

1 <= 차의 수 < 10,000
routes의 0번째 인덱스 : 고속도로에 진입한 지점
routes의 1번째 인덱스 : 고속도로에서 나간 지점

차량의 진입, 진출 지점에 카메라가 설치되어도 카메라를 만난 것으로 간주
차량의 진입, 진출 지점은 -30,000 이상 30,000 이하
"""

def solution(routes):
    

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]