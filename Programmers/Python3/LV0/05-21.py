# 문자열 정렬하기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120911
def solution(my_string):
    return "".join(sorted(my_string.lower()))


# 배열에서 문자열 대소문자 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181875
def solution(strArr):
    return [strArr[i].lower() if i % 2 == 0 else strArr[i].upper() for i in range(len(strArr))]


# 소문자로 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/181876
def solution(myString):
    return myString.lower()


# 원하는 문자열 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181878
def solution(myString, pat):
    return 1 if pat.lower() in myString.lower() else 0


# 길이에 따른 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/181879
def solution(num_list):
    answer = 1
    if len(num_list) > 10 :
        return sum(num_list)
    else :
        for i in num_list :
            answer *= i
    return answer


# 조건에 맞게 수열 변환하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181882
def solution(arr):
    return [i//2 if i >= 50 and i % 2 == 0 else i*2 if i <= 50 and i % 2 != 0 else i for i in arr]


# n보다 커질 때까지 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181884
def solution(numbers, n):
    answer = 0
    for i in numbers :
        if answer > n :
            return answer
        else :
            answer += i
    return answer


# 할 일 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/181885
def solution(todo_list, finished):
    return [v for i,v in enumerate(todo_list) if not finished[i]]


# 5명씩
# https://school.programmers.co.kr/learn/courses/30/lessons/181885
def solution(names):
    return names[::5]


# 순서 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/181891
def solution(num_list, n):
    return num_list[n:] + num_list[:n]