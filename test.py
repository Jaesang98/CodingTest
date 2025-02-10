def solution(n):
    if n > 6 :
        return (n % 6) + 1
    elif n < 6 :
        if 6 % n == 0 :
            return 6 / n
        else :
            return 6 % n
    return 1

print(solution(3))