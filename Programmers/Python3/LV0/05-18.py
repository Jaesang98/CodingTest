# 피자 나눠 먹기 (3)
# https://school.programmers.co.kr/learn/courses/30/lessons/120816?language=python3
import math
def solution(slice, n):
    return math.ceil(n / slice)


# 점의 위치 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120841?language=python3
def solution(dot):
    if dot[0] > 0 and dot[1] > 0 :
        return 1
    elif dot[0] < 0 and dot[1] > 0 :
        return 2
    elif dot[0] < 0 and dot[1] < 0 :
        return 3
    else :
        return 4


# 아이스 아메리카노
# https://school.programmers.co.kr/learn/courses/30/lessons/120819?language=python3
def solution(money):
    return [money // 5500, money % 5500]


# 홀짝 구분하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181944?language=python3
a = int(input())
print(f'{a} is even' if a % 2 == 0 else f'{a} is odd')


# 카운트 업
# https://school.programmers.co.kr/learn/courses/30/lessons/181920?language=python3
def solution(start_num, end_num):
    return [int(i) for i in range(start_num, end_num+1)]


# 첫 번째로 나오는 음수
# https://school.programmers.co.kr/learn/courses/30/lessons/181896?language=python3
def solution(num_list):
    for i in num_list :
        if i < 0 : 
            return num_list.index(i)
    return -1


# 공배수
# https://school.programmers.co.kr/learn/courses/30/lessons/181936?language=python3
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0


# 문자열의 뒤의 n글자
# https://school.programmers.co.kr/learn/courses/30/lessons/181910?language=python3
def solution(my_string, n):
    return my_string[-n:]


# 문자 리스트를 문자열로 변환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181941?language=python3
def solution(arr):
    return ''.join(arr)


# 두 수의 연산값 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181938?language=python3
def solution(a, b):
    return 2 * a * b if 2 * a * b > int(str(a)+str(b)) else int(str(a)+str(b))