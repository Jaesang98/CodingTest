# K번째수
# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 슬라이스 / sorted
def solution(array, commands):
    answer = []
    for i in commands :
        answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
    return answer
        