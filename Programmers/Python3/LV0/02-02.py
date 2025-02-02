# 개미 군단
# 개미 군단이 사냥을 나가려고 합니다. 개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다. 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다. 예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만, 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다. 사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120837
def solution(hp):
    if hp % 5 == 0 :
        return hp // 5
    else :
        if hp % 5 % 3 == 0 :
            return hp // 5 +  hp % 5 // 3
        else :
            return hp // 5 +  hp % 5 // 3 + hp % 5 % 3


# 가위 바위 보
# 가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120839
def solution(rsp):
    answer = ''
    for i in rsp :
        if i == "2" :
            answer += "0"
        elif i == "0" :
            answer += "5"
        else :
            answer += "2"
    return answer


# 숨어있는 숫자의 덧셈 (1)
# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120851
def solution(my_string):
    answer = 0
    for i in my_string :
        for j in range(1,10) :
            if i == str(j) :
                answer += j
    
    return answer


# 대문자와 소문자
# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120893
def solution(my_string):
    answer = ''
    for i in my_string :
        if i.isupper() :
            answer += i.lower()
        else :
            answer += i.upper()
    return answer


# 인덱스 바꾸기
# 문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120895
def solution(my_string, num1, num2):
    answer = ''
    for i in range(0,len(my_string)) :
        if i == num1 :
            answer += my_string[num2]
        elif i == num2 :
            answer += my_string[num1]
        else :
            answer += my_string[i]
    return answer


# 약수 구하기
# 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120897
def solution(n):
    answer = []
    for i in range(1,n+1) :
        if n % i == 0 :
            answer.append(i)
    return answer


# 가장 큰 수 찾기
# 정수 배열 array가 매개변수로 주어질 때, 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120899
def solution(array):
    answer = []
    answer.append(max(array))
    for i in range(0, len(array)) :
        if answer[0] == array[i]:
            answer.append(i)
    return answer


# 문자열로 변환
# 정수 n이 주어질 때, n을 문자열로 변환하여 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181845
def solution(n):
    return str(n)


# 문자열을 정수로 변환하기
# 숫자로만 이루어진 문자열 n_str이 주어질 때, n_str을 정수로 변환하여 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181848
def solution(n_str):
    return int(n_str) 


# 문자열 정수의 합
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181849
def solution(num_str):
    answer = 0
    for i in num_str :
        answer += int(i)
    return answer