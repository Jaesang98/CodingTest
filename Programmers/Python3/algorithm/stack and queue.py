# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# stack개념을 활용
def solution(arr):
    answer = [arr[0]]
    for i in arr :
        if answer[-1] != i :
            answer.append(i)
    return answer