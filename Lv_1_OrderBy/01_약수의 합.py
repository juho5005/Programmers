def solution(n):
    # 약수 구하기
    def aliquot(n) :
        sum_of_aliquots = 0

        for i in range(1, n+1) :
            if n % i == 0 :
                sum_of_aliquots += i 

        return sum_of_aliquots
    return aliquot(n)