# 배열 만들기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181895
def solution(n):
    answer = [n]
    while n != 1 :
        if n % 2 == 0 :
            n = n // 2
        else :
            n = 3 * n + 1
        answer.append(n)
    return answer


# 수 조작하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181926
def solution(n, control):
    for i in control :
        if i == "w" :
            n += 1
        elif i == "s" :
            n -= 1
        elif i == "d" :
            n += 10
        else :
            n -= 10
    return n


# 마지막 두 원소
# https://school.programmers.co.kr/learn/courses/30/lessons/181927
def solution(num_list):
    if num_list[-1] > num_list[-2] :
        num_list.append(num_list[-1] - num_list[-2])
    else :
        num_list.append(num_list[-1]*2)
    return num_list


# 문자열 돌리기
# https://school.programmers.co.kr/learn/courses/30/lessons/181945
str = input()
for i in str :
    print(i)


# 덧셈식 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181947
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')


# A 강조하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181874
def solution(myString):
    answer = ""
    for i in myString :
        if i == "a" or i == "A" :
            answer += i.upper()
        else :
            answer += i.lower()
    return answer


# 간단한 식 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181865
def solution(binomial):
    binomial = binomial.split()
    if binomial[1] == "+" :
        return int(binomial[0]) + int(binomial[2])
    elif binomial[1] == "-" :
        return int(binomial[0]) - int(binomial[2])
    else :
        return int(binomial[0]) * int(binomial[2])


# 특정한 문자를 대문자로 바꾸기
# https://school.programmers.co.kr/learn/courses/30/lessons/181873
def solution(my_string, alp):
    if alp in my_string :
        my_string = my_string.replace(alp, alp.upper())
    return my_string


# 주사위 게임 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181930
def solution(a, b, c):
    if a == b and b == c:
        return  (a + b + c) * (a**2 + b**2 + c**2 ) * (a**3 + b**3 + c**3 )
    elif a == b or b == c or a == c:
        return  (a + b + c) * (a**2 + b**2 + c**2 )
    else :
        return a + b + c 


# 수 조작하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181925
def solution(numLog):
    answer = ""
    for i in range(1, len(numLog)) :
        if numLog[i-1] - numLog[i] == 1 :
            answer += "s"
        elif numLog[i-1] - numLog[i] == -1 :
            answer += "w"
        elif numLog[i-1] - numLog[i] == 10 :
            answer += "a"
        else :
            answer += "d"
    return answer