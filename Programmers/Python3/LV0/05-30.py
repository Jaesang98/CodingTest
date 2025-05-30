# 이차원 배열 대각선 순회하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181829
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])) :
            if i + j <= k :
                answer +=  board[i][j]
    return answer


# 중복된 문자 제거
# https://school.programmers.co.kr/learn/courses/30/lessons/120888
def solution(my_string) :
    answer = ""
    for i in my_string :
        if i not in answer :
            answer += i
    return answer


# 등차수열의 특정한 항만 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181931
def solution(a, d, included):
    answer = 0
    for i in range(len(included)) :
        if included[i] :
            answer += a+d*i
    return answer


# 배열 만들기 5
# https://school.programmers.co.kr/learn/courses/30/lessons/181912
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        if int(i[s:s+l]) > k :
            answer.append(int(i[s:s+l]))
    return answer


# 글자 지우기
# https://school.programmers.co.kr/learn/courses/30/lessons/181900
def solution(my_string, indices):
    my_string = list(my_string)
    answer = ""
    
    for i in indices :
        my_string[i] = 0
        
    for i in my_string :
        if i != 0 :
            answer += i
    
    return answer