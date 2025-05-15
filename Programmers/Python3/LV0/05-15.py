# 두 수의 곱 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120804?language=python3
def solution(num1, num2):
    return num1 * num2


# 나머지 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120810?language=python3
def solution(num1, num2):
    return num1 % num2


# 두 수의 차 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120803?language=python3
def solution(num1, num2):
    return num1 - num2


# 숫자 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120807?language=python3
def solution(num1, num2):
    return 1 if num1 == num2 else -1


# 나이 출력
# https://school.programmers.co.kr/learn/courses/30/lessons/120820?language=python3
def solution(age):
    return 2023 - age


# 몫 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120805?language=python3
def solution(num1, num2):
    return num1 // num2


# 두 수의 합 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120802?language=python3
def solution(num1, num2):
    return num1 // num2


# 두 수의 나눗셈
# https://school.programmers.co.kr/learn/courses/30/lessons/120806?language=python3
def solution(num1, num2):
    return int(num1 / num2 * 1000)


# 각도기
# https://school.programmers.co.kr/learn/courses/30/lessons/120829?language=python3
def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle < 180:
        return 3
    else:
        return 4


# 양꼬치
# https://school.programmers.co.kr/learn/courses/30/lessons/120830?language=python3
def solution(n, k):
    return n * 12000 + k * 2000 - n//10 * 2000