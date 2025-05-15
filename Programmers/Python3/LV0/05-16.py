# 짝수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/120831?language=python3
def solution(n):
    answer = 0
    for i in range(0, n+1, 2): 
        answer += i
    return answer


# 배열의 유사도
# https://school.programmers.co.kr/learn/courses/30/lessons/120903?language=python3
def solution(s1, s2):
    answer = 0
    for i in s1 :
        if i in s2 :
            answer += 1
    return answer


# 문자열안에 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/120908?language=python3
def solution(str1, str2):
    return 1 if str2 in str1 else 2


# 배열의 평균값
# https://school.programmers.co.kr/learn/courses/30/lessons/120817?language=python3
def solution(numbers):
    return sum(numbers) / len(numbers)


# 배열 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/120821?language=python3
def solution(numbers):
    return sum(numbers) / len(numbers)


# 제곱수 판별하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120909?language=python3
def solution(n):
    return 1 if int(n ** 0.5) ** 2 == n else 2


# 짝수 홀수 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120824?language=python3
def solution(num_list):
    answer = [0,0]
    for i in num_list :
        if i % 2 == 0 :
            answer[0] += 1
        else :
            answer[1] += 1
    return answer


# 특정 문자 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120826?language=python3
def solution(my_string, letter):
    return my_string.replace(letter , '')


# 뒤집힌 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/120822?language=python3
def solution(my_string):
    return my_string[::-1]


# 문자 반복 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120825?language=python3
def solution(my_string, n):
    answer = ''
    for i in my_string :
        answer += i*n
    return answer