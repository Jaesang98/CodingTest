# 편지
# https://school.programmers.co.kr/learn/courses/30/lessons/120898?language=python3
def solution(message):
    return len(message) * 2


# 피자 나눠 먹기 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120814?language=python3
def solution(n):
    return (n+6) // 7


# 순서쌍의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120836?language=python3
def solution(n):
    answer = 0
    for i in range(1,n+1) :
        if n%i == 0 :
            answer +=1
    return answer


# 세균 증식
# https://school.programmers.co.kr/learn/courses/30/lessons/120910?language=python3
def solution(n, t):
    return n * 2 ** t 


# 최댓값 만들기(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120847?language=python3
def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]


# 모음 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120849?language=python3
def solution(my_string):
    answer = ''
    for i in my_string :
        if i not in ['a', 'e', 'i', 'o', 'u'] :
            answer += i
    return answer


# 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120906?language=python3
def solution(n):
    return sum([int(i) for i in str(n)])


# 머쓱이보다 키 큰 사람
# https://school.programmers.co.kr/learn/courses/30/lessons/120585?language=python3
def solution(array, height):
    return len([i for i in array if i > height ])


# 삼각형의 완성조건 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120889?language=python3
def solution(sides):
    sides.sort()
    return 1 if sides[-1] < sides[0] + sides[1] else 2


# 배열 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/120833?language=python3
def solution(numbers, num1, num2):
    return numbers[num1 : num2+1]