# 문자열 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120902
def solution(my_string):
    return eval(my_string)


# 문자열 여러 번 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/181913
def solution(my_string, queries):
    my_string = list(my_string)
    for i in queries :
        if i[0] == 0 :
            my_string[i[0]:i[1]+1] = my_string[i[1]::-1]
        else :
            my_string[i[0]:i[1]+1] = my_string[i[1]:i[0]-1:-1]
    return "".join(my_string)