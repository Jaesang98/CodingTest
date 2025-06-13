# 왼쪽 오른쪽
# https://school.programmers.co.kr/learn/courses/30/lessons/181890#
def solution(str_list):
    if "l" not in str_list and "r" not in str_list :
        return []
    else :
        for i in range(len(str_list)) :
            if str_list[i] == "l" :
                return str_list[:i]
            elif str_list[i] == "r" :
                return str_list[i+1:]


# 조건 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181934
def solution(ineq, eq, n, m):
    if ineq == "<" :
        if eq == "=" :
            return int(n <= m)
        else :
            return int(n < m)
    else :
        if eq == "=" :
            return int(n >= m)
        else :
            return int(n > m)