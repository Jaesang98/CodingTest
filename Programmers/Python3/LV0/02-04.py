# 조건에 맞게 수열 변환하기 1
# 정수 배열 arr가 주어집니다. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다. 그 결과인 정수 배열을 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181882
def solution(arr):
    answer = []
    for i in arr :
        if i >= 50 and i % 2 == 0:
            answer.append(i/2)
        elif i < 50 and i % 2 != 0:
            answer.append(i*2)
        else :
            answer.append(i)
    return answer


# n보다 커질 때까지 더하기
# 정수 배열 numbers와 정수 n이 매개변수로 주어집니다. numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 하는 solution 함수를 작성해 주세요.
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
# 오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때, todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181885
def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)) :
        if not finished[i] :
            answer.append(todo_list[i])
    return answer


# 5명씩
# 최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담긴 문자열 리스트 names가 주어질 때, 앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 사람들의 이름을 담은 리스트를 return하도록 solution 함수를 완성해주세요. 마지막 그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/181886
def solution(names):
    answer = []
    for i in range(0,len(names),5) :
        answer.append(names[i])
    return answer


# 홀수 vs 짝수
# 정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/181887
def solution(num_list):
    answer = 0
    answer2 = 0
    for i in range(0, len(num_list), 2) :
        answer += num_list[i]
    for i in range(1, len(num_list), 2) :
        answer2 += num_list[i]
    return max(answer,answer2)


# n개 간격의 원소들
# 정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 마지막 원소까지 n개 간격으로 저장되어있는 원소들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181888
def solution(num_list, n):
    return num_list[0:len(num_list):n]


# n 번째 원소까지
# 정수 리스트 num_list와 정수 n이 주어질 때, num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181889
def solution(num_list, n):
    return num_list[0:n]


# 순서 바꾸기
# 정수 리스트 num_list와 정수 n이 주어질 때, num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181891
def solution(num_list, n):
    answer = num_list[n:]
    for i in num_list[0:n] :
        answer.append(i)
    return answer


# n 번째 원소부터
# 정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181892
def solution(num_list, n):
    return num_list[n-1 : len(num_list)]


# 첫 번째로 나오는 음수
# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/181896
def solution(num_list):
    for i in num_list :
        if i < 0 :
            return num_list.index(i)
    return -1


# 가까운 1 찾기
# 정수 배열 arr가 주어집니다. 이때 arr의 원소는 1 또는 0입니다. 정수 idx가 주어졌을 때, idx보다 크면서 배열의 값이 1인 가장 작은 인덱스를 찾아서 반환하는 solution 함수를 완성해 주세요. 단, 만약 그러한 인덱스가 없다면 -1을 반환합니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/181898
def solution(arr, idx):
    answer = -1
    for i in range(len(arr)) :
        if idx <= i and arr[i] == 1:
            return i
    return answer