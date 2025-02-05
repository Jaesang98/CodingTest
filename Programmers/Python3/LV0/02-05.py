# 카운트 다운
# 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181899
def solution(start_num, end_num):
    answer = []
    for i in range(start_num , end_num-1, -1) :
        answer.append(i)
    return answer


# 배열 만들기 1
# 정수 n과 k가 주어졌을 때, 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열을 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181901
def solution(n, k):
    answer = []
    for i in range(k,n+1,k) :
        answer.append(i)
    return answer


# 접두사인지 확인하기
# 어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다. 문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181906
def solution(my_string, is_prefix):
    answer = ''
    if len(is_prefix) > len(my_string) :
        return 0
    else :
        for i in range(len(is_prefix)) :
            answer += my_string[i]
        
    if answer == is_prefix :
        return 1 
    else :
        return 0


# 문자열의 앞의 n글자
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181907
def solution(my_string, n):
    return my_string[:n]


# 문자열의 뒤의 n글자
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181910
def solution(my_string, n):
    return my_string[len(my_string)-n:len(my_string)]


# 부분 문자열 이어 붙여 문자열 만들기
# 길이가 같은 문자열 배열 my_strings와 이차원 정수 배열 parts가 매개변수로 주어집니다. parts[i]는 [s, e] 형태로, my_string[i]의 인덱스 s부터 인덱스 e까지의 부분 문자열을 의미합니다. 각 my_strings의 원소의 parts에 해당하는 부분 문자열을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181911
def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)) :
        answer += my_strings[i][parts[i][0]:parts[i][1]+1]
    return answer


# 글자 이어 붙여 문자열 만들기
# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181915
def solution(my_string, index_list):
    answer = ''
    for i in index_list :
        answer += my_string[i]
    return answer


# 카운트 업
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181920
def solution(start_num, end_num):
    answer = []
    for i in range(start_num , end_num+1):
        answer.append(i)
    return answer


# 마지막 두 원소
# 정수 리스트 num_list가 주어질 때, 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가하여 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181927
def solution(num_list):
    answer = num_list
    if num_list[len(num_list)-1] > num_list[len(num_list)-2] :
        answer.append(num_list[len(num_list)-1] - num_list[len(num_list)-2])
    else :
        answer.append(num_list[len(num_list)-1]*2)
    return answer