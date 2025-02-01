# n의 배수 고르기
# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120905
def solution(n, numlist):
    answer = []
    for i in numlist :
        if i % n == 0 :
            answer.append(i)
    return answer


# 홀짝 구분하기
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181944
a = int(input())

if a % 2 == 0 :
    print(str(a) + " is even")
else :
    print(str(a) + " is odd")


# flag에 따라 다른 값 반환하기
# 두 정수 a, b와 boolean 변수 flag가 매개변수로 주어질 때, flag가 true면 a + b를 false면 a - b를 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181933
def solution(a, b, flag):
    if flag == True :
        return a + b
    else :
        return a - b


# 문자열 붙여서 출력하기
# 두 개의 문자열 str1, str2가 공백으로 구분되어 입력으로 주어집니다. 입출력 예와 같이 str1과 str2을 이어서 출력하는 코드를 작성해 보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181946
str1, str2 = input().strip().split(' ')
print(str1 + str2)


# 중앙값 구하기
# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120811
def solution(array):
    array.sort()
    answer = array[len(array)//2]
    return answer


# 짝수는 싫어요
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120813
def solution(n):
    answer = []
    for i in range(1,n+1) :
        if i % 2 != 0:
            answer.append(i)
    return answer


# 직각삼각형 출력하기
# "*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 직각 이등변 삼각형을 그리려고합니다. 정수 n 이 주어지면 높이와 너비가 n 인 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120823
n = int(input())
for i in range(1,n+1) :
    print('*' * i)


# 홀짝에 따라 다른 값 반환하기
# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181935
def solution(n):
    answer = 0
    if n % 2 == 0 :
        for i in range(1,n+1) :
            if i % 2 == 0 :
                answer += i*i
    else :
        for i in range(1,n+1) :
            if i % 2 != 0 :
                answer += i
    return answer


# 이어 붙인 수
# 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181928
def solution(num_list):
    answer = 0
    jjack = ''
    hole = ''
    for i in num_list:
        if i % 2 == 0 :
            jjack += str(i)
        else :
            hole += str(i)
    answer = int(jjack) + int(hole)
    return answer


# 옷가게 할인 받기
# 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다. 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120818
def solution(price):
    if price >= 100000 and price < 300000:
        return int(price - price*0.05)
    elif price >= 300000 and price < 500000:
        return int(price - price*0.1)
    elif price >= 500000:
        return int(price - price*0.2)
    else: 
        return price