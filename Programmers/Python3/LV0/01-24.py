# 세균 증식
# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120910
def solution(n, t):
    answer = n
    for i in range(0,t) :
        answer = answer * 2
    return answer


# 자릿수 더하기
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요
# https://school.programmers.co.kr/learn/courses/30/lessons/120906
def solution(n):
    answer = 0
    for i in str(n) :
        answer += int(i)
    return answer


# 모음 제거
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120849
def solution(my_string):
    moem = ['a', 'e', 'i', 'o', 'u']
    for i in moem :
        my_string = my_string.replace(i, '')
    return my_string


# 특정 문자 제거하기
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120826
def solution(my_string, letter):
    answer = my_string.replace(letter, '')
    return answer


# 순서쌍의 개수
# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120836
def solution(n):
    answer = 0
    for i in range(1,n+1) :
        if n%i == 0:
            answer += 1
    return answer


# 문자 반복 출력하기
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120825
def solution(my_string, n):
    answer = ''
    for i in my_string :
        answer += i * n
    return answer


# 배열 자르기
# 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120833
def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2+1) :
        answer.append(numbers[i])
    return answer


# 피자 나눠 먹기 (1)
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120814
def solution(n):
    if n % 7 == 0 :
        return n / 7
    elif n % 7 != 0 :
        if n <= 7 : 
            return 1
        else :
            return int(n/7) + 1


# 짝수 홀수 개수
# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120824
def solution(num_list):
    answer = [0,0]
    for i in num_list :
        if i % 2 == 0 :
            answer[0] += 1
        else :
            answer[1] += 1
    return answer


# 두 수의 합
# 정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120802
def solution(num1, num2):
    answer = num1 + num2
    return answer


# 문자열 뒤집기
# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120822
def solution(my_string):
    answer = ''
    for i in my_string :
        answer = i + answer
    return answer


# 점의 위치 구하기
# x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120841
def solution(dot):
    if (dot[0] > 0) & (dot[1] > 0) :
        return 1
    elif (dot[0] < 0) & (dot[1] > 0) :
        return 2
    elif (dot[0] < 0) & (dot[1] < 0) :
        return 3
    else :
        return 4


# 아이스 아메리카노
# 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다. 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120819
def solution(money):
    answer = [int(money/5500), int(money%5500)]
    return answer


# 삼각형의 완성조건 (1)
# 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다. 삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120889
def solution(sides):
    answer = 0
    sides.sort(reverse=True)
    
    for i in range(1,len(sides)) :
        answer += sides[i]
    
    if sides[0] >= answer:
        return 2
    else :
        return 1


# 중복된 숫자 개수
# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120583
def solution(array, n):
    answer = 0
    for i in array :
        if n == i :
            answer += 1
    return answer


# 배열 두 배 만들기
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120809
def solution(numbers):
    answer = []
    for i in numbers :
        answer.append(i*2)
    return answer


# n의 배수
# 정수 num과 n이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return n의 배수가 아니라면 0을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181937
def solution(num, n):
    if num % n == 0:
        return 1
    else :
        return 0


# 공배수
# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181936
def solution(number, n, m):
    if (number % n == 0) & (number % m == 0) :
        return 1
    else :
        return 0


# [PCCE 기출문제] 1번 / 문자 출력
# 주어진 코드는 변수에 데이터를 저장하고 출력하는 코드입니다. 아래와 같이 출력되도록 빈칸을 채워 코드를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/340207
message = "Let's go!"
print("3\n2\n1")
print(message)