# 중복된 숫자 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120583?language=python3
def solution(array, n):
    return array.count(n)


# 배열 두 배 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120809?language=python3
def solution(numbers):
    return [i*2 for i in numbers]


# 배열 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/120821?language=python3
def solution(num_list):
    num_list.reverse()
    return num_list


# 중앙값 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120811?language=python3
def solution(array):
    array.sort()
    return array[len(array) // 2 :len(array) // 2 + 1][0]


# 짝수는 싫어요
# https://school.programmers.co.kr/learn/courses/30/lessons/120813?language=python3
def solution(n):
    return [x for x in range(n+1) if x % 2 == 1]


# 옷가게 할인 받기
# https://school.programmers.co.kr/learn/courses/30/lessons/120818?language=python3
def solution(price):
    if price < 100000 :
        return price
    elif price < 300000 :
        return int(price * 0.95)
    elif price < 500000 :
        return int(price * 0.9)
    else :
        return int(price * 0.8)


# 개미 군단
# https://school.programmers.co.kr/learn/courses/30/lessons/120837?language=python3
def solution(hp):
    return (hp // 5) + (hp % 5 // 3) + (hp % 5 % 3)


# 가위 바위 보
# https://school.programmers.co.kr/learn/courses/30/lessons/120839?language=python3
def solution(rsp):
    return ''.join(["0" if i == "2" else "5" if i == "0" else "2" for i in rsp])


# 문자열 정렬하기 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120850?language=python3
def solution(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])


# 숨어있는 숫자의 덧셈 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120851?language=python3
def solution(my_string):
    return sum([int(i) for i in my_string if i.isdigit()])


# 암호 해독
# https://school.programmers.co.kr/learn/courses/30/lessons/120892?language=python3
def solution(cipher, code):
    return cipher[code-1::code]


# 대문자와 소문자
# https://school.programmers.co.kr/learn/courses/30/lessons/120893?language=python3
def solution(my_string):
    return my_string.swapcase()


# 배열 원소의 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/120854?language=python3
def solution(strlist):
    return [len(i) for i in strlist]


# n의 배수 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/120905?language=python3
def solution(n, numlist):
    return [i for i in numlist if i%n == 0]


# 첫 번째로 나오는 음수
# https://school.programmers.co.kr/learn/courses/30/lessons/120905?language=python3
def solution(n, numlist):
    return [i for i in numlist if i%n == 0]


# [PCCE 기출문제] 5번 / 산책
# https://school.programmers.co.kr/learn/courses/30/lessons/250129
def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S" :
            north -= 1
        elif i == "E" :           
            east += 1
        elif i == "W":  
            east -= 1
    return [east, north]


# [PCCE 기출문제] 4번 / 저축
# https://school.programmers.co.kr/learn/courses/30/lessons/250130
start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100:
    money += after
    month += 1

print(month)


# [PCCE 기출문제] 2번 / 피타고라스의 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/250132
a = int(input())
c = int(input())

b_square = c*c - a*a
print(b_square)


# [PCCE 기출문제] 1번 / 출력
# https://school.programmers.co.kr/learn/courses/30/lessons/250133
string_msg = "Spring is beginning"
int_val = 3
string_val = "3"

print(string_msg)
print(int_val + 10)
print(string_val + "10")


# [PCCE 기출문제] 3번 / 나이 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/250131
year = int(input())
age_type = input()

if age_type == 'Korea':
    answer = 2031-year
elif age_type == "Year":
    answer = 2030-year

print(answer)


# [PCCE 기출문제] 6번 / 가채점
# https://school.programmers.co.kr/learn/courses/30/lessons/250128
def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i]-1]:
            answer.append("Same")
        else:
            answer.append("Different")
    
    return answer