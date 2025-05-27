# 문자열 붙여서 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181946
str1, str2 = input().strip().split(' ')
print(str1 + str2)


# 뒤에서 5등 위로
# https://school.programmers.co.kr/learn/courses/30/lessons/181852
def solution(num_list):
    return sorted(num_list)[5:]


# 문자열로 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/181845
def solution(n):
    return str(n)


# 문자열 정수의 합
# https://school.programmers.co.kr/learn/courses/30/lessons/181849
def solution(num_str):
    answer = 0
    for i in num_str :
        answer += int(i)
    return answer


# 문자열을 정수로 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181848
def solution(n_str):
    return int(n_str)


# 뒤에서 5등까지
# https://school.programmers.co.kr/learn/courses/30/lessons/181853
def solution(num_list):
    return sorted(num_list)[:5]


# 배열의 길이에 따라 다른 연산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181854
def solution(arr, n):
    if len(arr) % 2 == 0 :
        for i in range(1,len(arr),2) :
            arr[i] += n 
    else :
        for i in range(0,len(arr),2) :
            arr[i] += n 
    return arr


# 부분 문자열인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181843
def solution(my_string, target):
    return 1 if target in my_string else 0 


# 특별한 이차원 배열 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181833
def solution(n):
    answer = [[0] * n for _ in range(n)]
    for i in range(n) :
        answer[i][i] = 1
    return answer


# 특별한 이차원 배열 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181831
def solution(arr):
    for i in range(len(arr)) :
        for j in range(len(arr[0])) :
            if arr[i][j] != arr[j][i] :
                return 0
    return 1