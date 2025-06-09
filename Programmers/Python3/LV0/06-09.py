# 7의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120912
def solution(array):
    answer = 0
    for i in array :
        answer += str(i).count("7")
    return answer


# 가까운 수
# https://school.programmers.co.kr/learn/courses/30/lessons/120890
def solution(array, n):
    array.append(n)
    array.sort()
    index = array.index(n)
    
    if index == 0 :
        return array[1]
    elif index == len(array)-1 :
        return array[-2]
    else :
        if array[index] - array[index-1] > array[index+1] - array[index] :
            return array[index+1]
        else :
            return array[index-1]


# 팩토리얼
# https://school.programmers.co.kr/learn/courses/30/lessons/120848
def solution(n):
    answer = 1
    def factorial(i) : 
        nonlocal answer
        if answer * i > n :
            return i-1
        answer *= i
        return factorial(i+1)
    return factorial(1)


# 숨어있는 숫자의 덧셈 (2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120864
def solution(my_string):
    answer = []
    count = ""
    for i in my_string :
        if i.isalpha() :
            answer.append(count)
            count = ""
        else :
            count += i
    
    if count :
        answer.append(count)
    
    return sum([int(i) for i in  answer if i != ""])


# 진료순서 정하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120835
def solution(emergency):
    answer = sorted(emergency, reverse=True)
    return [answer.index(x) + 1 for x in emergency]
