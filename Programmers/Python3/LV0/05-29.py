# 공백으로 구분하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181869
def solution(my_string):
    return my_string.split()


# 원소들의 곱과 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181929
def solution(num_list):
    a = 0
    b = 1
    for i in num_list :
        a += i
        b *= i
    return 1 if a**2 > b else 0


# n개 간격의 원소들
# https://school.programmers.co.kr/learn/courses/30/lessons/181888
def solution(num_list, n):
    return num_list[::n]


# 접미사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181908
def solution(my_string, is_suffix):
    answer = ""
    for i in range(len(my_string)-1,-1,-1) :
        answer = my_string[i:]
        if is_suffix == answer :
            return 1
    return 0


# 더 크게 합치기
# https://school.programmers.co.kr/learn/courses/30/lessons/181939
def solution(a, b):
    return int(str(a) + str(b)) if str(a) + str(b) > str(b) + str(a) else int(str(b) + str(a))


# n 번째 원소까지
# https://school.programmers.co.kr/learn/courses/30/lessons/181889
def solution(num_list, n):
    return num_list[:n]


# 369게임
# https://school.programmers.co.kr/learn/courses/30/lessons/120891
def solution(order):
    answer = 0
    for i in str(order) :
        if i == "3" :
            answer +=1
        elif i == "6" :
            answer +=1
        elif i == "9" :
            answer +=1
    return answer


# 배열 회전시키기
# https://school.programmers.co.kr/learn/courses/30/lessons/120844?language=python3
def solution(order):
    answer = 0
    for i in str(order) :
        if i == "3" :
            answer +=1
        elif i == "6" :
            answer +=1
        elif i == "9" :
            answer +=1
    return answer


# 외계행성의 나이
# https://school.programmers.co.kr/learn/courses/30/lessons/120834
def solution(age):
    answer = 'abcdefghij'
    return "".join([answer[int(i)] for i in str(age)])


# 문자열 잘라서 정렬하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181866
def solution(myString):
    return sorted([i for i in myString.split("x") if i])