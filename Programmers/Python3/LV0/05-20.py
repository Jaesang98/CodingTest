# n의 배수
# https://school.programmers.co.kr/learn/courses/30/lessons/181937
def solution(num, n):
    return 1 if num % n == 0 else 0


# 대문자로 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/181877
def solution(myString):
    return myString.upper()


# 홀짝에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181935
def solution(n):
    return sum([i for i in range(1,n+1,2)]) if n % 2 != 0 else sum([i**2 for i in range(0,n+1,2)])


# 문자열 곱하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181940
def solution(my_string, k):
    return my_string * k


# n 번째 원소부터
# https://school.programmers.co.kr/learn/courses/30/lessons/181892
def solution(num_list, n):
    return num_list[n-1:]


# 직각삼각형 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120823
n = int(input())
for i in range(1,n+1) :
    print('*' * i)


# 주사위의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120845
def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n) 


# 약수 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120897
def solution(n):
    return [i for i in range(1,n+1) if n % i == 0]


# 가장 큰 수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120899
def solution(array):
    return [max(array), array.index(max(array))]


# 인덱스 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/120895
def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return ''.join(my_string)