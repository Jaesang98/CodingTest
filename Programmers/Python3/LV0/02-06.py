# 최댓값 만들기 (2)
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120862
def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])


# 접미사인지 확인하기
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다. 문자열 my_string과 is_suffix가 주어질 때, is_suffix가 my_string의 접미사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181908
def solution(my_string, is_suffix):
    for i in range(0,len(my_string)) :
        if is_suffix == my_string[i:len(my_string)] :
            return 1
    return 0


# 접미사 배열
# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다. 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다. 문자열 my_string이 매개변수로 주어질 때, my_string의 모든 접미사를 사전순으로 정렬한 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181909
def solution(my_string):
    answer = []
    for i in range(0,len(my_string)) :
        answer.append(my_string[i:len(my_string)])
    return sorted(answer)


# 콜라츠 수열 만들기
# 모든 자연수 x에 대해서 현재 값이 x이면 x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1로 바꾸는 계산을 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제를 콜라츠 문제라고 부릅니다. 그리고 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열이라고 부릅니다. 계산 결과 1,000 보다 작거나 같은 수에 대해서는 전부 언젠가 1에 도달한다는 것이 알려져 있습니다. 임의의 1,000 보다 작거나 같은 양의 정수 n이 주어질 때 초기값이 n인 콜라츠 수열을 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181919
def solution(n):
    answer = [n]
    while n != 1: 
        if n % 2 == 0 :
            n = n/2
            answer.append(n)
        else :
            n = 3*n+1
            answer.append(n)
    return answer


# 수 조작하기 2
'''정수 배열 numLog가 주어집니다. 처음에 numLog[0]에서 부터 시작해 "w", "a", "s", "d"로 이루어진 문자열을 입력으로 받아 순서대로 다음과 같은 조작을 했다고 합시다.
"w" : 수에 1을 더한다.
"s" : 수에 1을 뺀다.
"d" : 수에 10을 더한다.
"a" : 수에 10을 뺀다.
그리고 매번 조작을 할 때마다 결괏값을 기록한 정수 배열이 numLog입니다. 즉, numLog[i]는 numLog[0]로부터 총 i번의 조작을 가한 결과가 저장되어 있습니다.
주어진 정수 배열 numLog에 대해 조작을 위해 입력받은 문자열을 return 하는 solution 함수를 완성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181925
def solution(numLog):
    answer = ''
    for i in range(0,len(numLog)) :
        if len(numLog) - 1 == i :
            return answer
        elif numLog[i] + 1 == numLog[i+1] :
            answer += 'w'
        elif numLog[i] - 1 == numLog[i+1] :
            answer += 's'
        elif numLog[i] + 10 == numLog[i+1] :
            answer += 'd'
        elif numLog[i] - 10 == numLog[i+1] :
            answer += 'a'
    return answer


# 수 조작하기 1
'''정수 n과 문자열 control이 주어집니다. control은 "w", "a", "s", "d"의 4개의 문자로 이루어져 있으며, control의 앞에서부터 순서대로 문자에 따라 n의 값을 바꿉니다.
"w" : n이 1 커집니다.
"s" : n이 1 작아집니다.
"d" : n이 10 커집니다.
"a" : n이 10 작아집니다.
위 규칙에 따라 n을 바꿨을 때 가장 마지막에 나오는 n의 값을 return 하는 solution 함수를 완성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181926
def solution(n, control):
    answer = n
    for i in control :
        if i == 'w' :
            answer += 1
        elif i == 's' :
            answer -= 1
        elif i == 'd' :
            answer += 10
        elif i == 'a' :
            answer -= 10
    return answer


# 최댓값 만들기 (2)
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120862
def solution(numbers):
    numbers.sort()
    return max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])


# 원소들의 곱과 합
# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181929
def solution(num_list):
    answer = 1
    for i in num_list :
        answer *= i
    
    if sum(num_list) ** 2 > answer :
        return 1
    else :
        return 0


# 문자 리스트를 문자열로 변환하기
# 문자들이 담겨있는 배열 arr가 주어집니다. arr의 원소들을 순서대로 이어 붙인 문자열을 return 하는 solution함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181941
def solution(arr):
    answer = ''
    for i in arr :
        answer += i
    return answer


# 문자열 돌리기
# 문자열 str이 주어집니다. 문자열을 시계방향으로 90도 돌려서 아래 입출력 예와 같이 출력하는 코드를 작성해 보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181945
str = input()
for i in str :
    print(i)


# 문자열 정렬하기 (1)
# 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120850
def solution(my_string):
    answer = []
    for i in range(0,10) :
        for j in my_string :
            if str(i) == j :
                answer.append(int(j))
    return sorted(answer)


# l로 만들기
# 알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181834
def solution(myString):
    answer = ''
    for i in myString :
        if i < 'l' :
            answer += 'l'
        else :
            answer += i
    return answer


# 암호 해독
'''군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.
암호화된 문자열 cipher를 주고받습니다.
그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/120892
def solution(cipher, code):
    return cipher[code-1 : len(cipher) : code]


# 간단한 식 계산하기
# 문자열 binomial이 매개변수로 주어집니다. binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181865
def solution(binomial):
    answer = binomial.split()

    if answer[1] == "+":
        result = int(answer[0]) + int(answer[2])
    elif answer[1] == "-":
        result = int(answer[0]) - int(answer[2])
    elif answer[1] == "*":
        result = int(answer[0]) * int(answer[2])
    elif answer[1] == "/":
        result = int(answer[0]) / int(answer[2])
    return result


# 9로 나눈 나머지
'''음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것이 알려져 있습니다.
이 사실을 이용하여 음이 아닌 정수가 문자열 number로 주어질 때, 이 정수를 9로 나눈 나머지를 return 하는 solution 함수를 작성해주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181914
def solution(number):
    answer = 0
    for i in number :
        answer += int(i)
    return answer % 9


# 덧셈식 출력하기
# 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요. a + b = c
# https://school.programmers.co.kr/learn/courses/30/lessons/181947
a, b = map(int, input().strip().split(' '))
print(f'{a} + {b} = {a + b}')


# 배열의 원소 삭제하기
# 정수 배열 arr과 delete_list가 있습니다. arr의 원소 중 delete_list의 원소를 모두 삭제하고 남은 원소들은 기존의 arr에 있던 순서를 유지한 배열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181844
def solution(arr, delete_list):
    answer = []
    for i in delete_list :
        if i in arr :
            arr.remove(i)
    return arr


# 공백으로 구분하기 1
# 단어가 공백 한 개로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181869
def solution(my_string):
    return my_string.split()


# 부분 문자열
'''어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.
문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181842
def solution(str1, str2):
    if str1 in str2 :
        return 1
    else :
        return 0


# 꼬리 문자열
'''문자열들이 담긴 리스트가 주어졌을 때, 모든 문자열들을 순서대로 합친 문자열을 꼬리 문자열이라고 합니다. 꼬리 문자열을 만들 때 특정 문자열을 포함한 문자열은 제외시키려고 합니다.
예를 들어 문자열 리스트 ["abc", "def", "ghi"]가 있고 문자열 "ef"를 포함한 문자열은 제외하고 꼬리 문자열을 만들면 "abcghi"가 됩니다.
문자열 리스트 str_list와 제외하려는 문자열 ex가 주어질 때, str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return하도록 solution 함수를 완성해주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181841
def solution(str_list, ex):
    answer = ''
    for i in str_list :
        if ex not in i :
            answer += i
    return answer