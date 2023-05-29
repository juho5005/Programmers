def solution(brown, yellow):
    def prime_nums(n) :
        for i in range(int(n**(1/2)), 0, -1) :
            if n % i == 0 :
                x, y = i, (n//i)

                if (((x+2)*2) + ((y+2)*2) -4) == brown :
                    if x > y :
                        return [x+2, y+2]
                    else :
                        return [y+2, x+2]

    return prime_nums(yellow)