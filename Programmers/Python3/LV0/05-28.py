# flag에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181933
def solution(a, b, flag):
    return a+b if flag else a-b


# 이어 붙인 수
# https://school.programmers.co.kr/learn/courses/30/lessons/181928
def solution(num_list):
    answer1 = ""
    answer2 = ""
    for i in num_list :
        if i % 2 == 0 :
            answer1 += str(i)
        else :
            answer2 += str(i)
    return int(answer1) + int(answer2) 


# 배열 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181856
def solution(arr1, arr2):
    if len(arr1) > len(arr2) :
        return 1
    elif len(arr1) < len(arr2) :
        return -1
    elif sum(arr1) > sum(arr2) :
        return 1
    elif sum(arr1) < sum(arr2) :
        return -1
    else :
        return 0


# 주사위 게임 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181839
def solution(a, b):
    if a % 2 != 0 and b % 2 != 0 :
        return a**2 + b**2
    elif a % 2 != 0 or b % 2 != 0 :
        return 2*(a+b)
    else :
        return abs(a-b)


# ad 제거하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181870?language=python3
def solution(strArr):
    answer = []
    for i in strArr :
        if "ad" not in i :
            answer.append(i)
    return answer


# 배열의 원소만큼 추가하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181861?language=python3
def solution(arr):
    answer = []
    for i in arr :
        answer += [i]*i
    return answer


# 홀수 vs 짝수
# https://school.programmers.co.kr/learn/courses/30/lessons/181887?language=python3
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))


# rny_string
# https://school.programmers.co.kr/learn/courses/30/lessons/181863?language=python3
def solution(rny_string):
    return rny_string.replace("m", "rn")


# 공백으로 구분하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181868?language=python3
def solution(my_string):
    return my_string.split()


# x 사이의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/181867?language=python3
def solution(myString):
    return [len(i) for i in myString.split("x")]