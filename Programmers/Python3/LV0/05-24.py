# 배열 만들기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181895
def solution(arr, intervals):
    return arr[intervals[0][0] : intervals[0][1]+1] + arr[intervals[1][0] : intervals[1][1]+1]


# 최댓값 만들기 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120862
def solution(numbers):
    numbers.sort()
    return max(numbers[-1]*numbers[-2], numbers[0]*numbers[1])


# 가까운 1 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181898
def solution(arr, idx):
    for i in range(idx, len(arr)) :       
        if arr[i] == 1 :
            return i
    return -1


# 카운트 다운
# https://school.programmers.co.kr/learn/courses/30/lessons/181899
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num-1, -1)]


# 배열 만들기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181901
def solution(n, k):
    return [i for i in range(k,n+1,k)]


# 접두사인지 확인하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181906
def solution(my_string, is_prefix):
    answer = [0] * len(my_string)
    answer[0] = my_string[0]
    for i in range(1,len(my_string)) :
        answer[i] = answer[i-1] + my_string[i]
    
    if is_prefix in answer :
        return 1
    else :
        return 0


# 접미사 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/181909
def solution(my_string):
    answer = [my_string[i:] for i in range(len(my_string))] 
    return sorted(answer)


# 부분 문자열 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181911
def solution(my_strings, parts):
    return ''.join([my_strings[i][parts[i][0]:parts[i][1]+1] for i in range(len(my_strings))])


# 9로 나눈 나머지
# https://school.programmers.co.kr/learn/courses/30/lessons/181914
def solution(number):
    return int(number) % 9


# 글자 이어 붙여 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181915
def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])


# 문자열의 앞의 n글자
# https://school.programmers.co.kr/learn/courses/30/lessons/181907
def solution(my_string, n):
    return my_string[:n]