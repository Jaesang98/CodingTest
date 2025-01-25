# 두수의 차
# 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120803
def solution(num1, num2):
    answer = num1 - num2
    return answer


# 숫자 비교하기
# 정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120807
def solution(num1, num2):
    if num1 == num2 : 
        return 1
    else : 
        return -1


# 나이 출력
# 머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 2022년 기준 선생님의 나이 age가 주어질 때, 선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요
# https://school.programmers.co.kr/learn/courses/30/lessons/120820
def solution(age):
    answer = 2022 - age+1
    return answer


# 나머지 구하기
# 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120810
def solution(num1, num2):
    answer = num1 % num2
    return answer


# 몫 구하기
# 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120810
def solution(num1, num2):
    answer = int(num1 / num2)
    return answer


# 두 수의 곱
# 정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120804
def solution(num1, num2):
    answer = num1 * num2
    return answer


# 두 수의 나눗셈
# 정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120806
def solution(num1, num2):
    answer = int(num1 / num2 * 1000)
    return answer


# 배열의 평균값
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120817
def solution(numbers):
    answer = 0;
    for i in numbers :
        answer += i 
    return answer / len(numbers)


# 각도기
# 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120829
def solution(angle):
    if angle < 90 :
        return 1
    elif angle == 90:
        return 2
    elif (angle > 90) & (angle < 180) :
        return 3
    else :
        return 4


# 양꼬치
# 머쓱이네 양꼬치 가게는 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 양꼬치는 1인분에 12,000원, 음료수는 2,000원입니다. 정수 n과 k가 매개변수로 주어졌을 때, 양꼬치 n인분과 음료수 k개를 먹었다면 총얼마를 지불해야 하는지 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120830
def solution(n, k):
    answer = (n * 12000) + (k * 2000) - (int(n/10) * 2000)
    return answer


# 짝수의 합
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120831
def solution(n):
    answer = 0;
    for i in range(0,n+1) :
        if(i%2 == 0) :
            answer += i;
    return answer


# 머쓱이보다 키 큰 사람
# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120585
def solution(array, height):
    answer = 0
    for i in array :
        if height < i :
            answer += 1;
    return answer


# 배열의 유사도
# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120903
def solution(s1, s2):
    answer = 0
    for i in s1 :
        for j in s2 :
            if i == j :
                answer +=1
    return answer


# 피자 나눠 먹기 (3)
# 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120816
def solution(slice, n):
    answer = 0;
    if n > slice :
        if n % slice == 0 :
            answer = n/slice
        else :
            answer = int(n/slice) + 1
    else :
        answer = 1
    return answer


# 배열 원소의 길이
# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120854
def solution(strlist):
    answer = []
    for i in strlist :
        answer.append(len(i))
    return answer


# 문자열안에 문자열
# 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120908
def solution(str1, str2):
    if str2 in str1 :
        return 1
    else :
        return 2


# 제곱수 판별하기
# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120909
def solution(n):
    if n % (n ** 0.5) == 0 :
        return 1
    else :
        return 2


# 배열 뒤집기
# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120821
def solution(num_list):
    num_list.reverse()
    return num_list