# 특별한 이차원 배열 1
# 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요. arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/181833
def solution(n):
    answer = []
    for i in range(n) :
        answer.append([]);
        
    for i in range(n) :
        for j in range(n) :
            if i == j :  
                answer[j].append(1)
            else :
                answer[j].append(0)
    return answer


# 주사위의 개수
# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 정수 n이 매개변수로 주어졌을 때, 상자에 들어갈 수 있는 주사위의 최대 개수를 return 하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120845
def solution(box, n):
    return (box[0] // n) * (box[1] // n) * (box[2] // n)


# 주사위 게임 1
'''1부터 6까지 숫자가 적힌 주사위가 두 개 있습니다. 두 주사위를 굴렸을 때 나온 숫자를 각각 a, b라고 했을 때 얻는 점수는 다음과 같습니다.
a와 b가 모두 홀수라면 a2 + b2 점을 얻습니다.
a와 b 중 하나만 홀수라면 2 × (a + b) 점을 얻습니다.
a와 b 모두 홀수가 아니라면 |a - b| 점을 얻습니다.
두 정수 a와 b가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181839
def solution(a, b):
    answer = 0
    if a % 2 != 0 and b % 2 != 0 :
        return a**2 + b**2
    elif a % 2 != 0 or b % 2 != 0 :
        return 2 * (a+b)
    else :
        if a > b :
            return a-b
        elif a < b :
            return b-a 
        else :
            return 0
    return answer


# 특별한 이차원 배열 2
# n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요. 0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]
# https://school.programmers.co.kr/learn/courses/30/lessons/181831
def solution(arr):
    answer = 1
    for i in range(len(arr)) :
        for j in range(i) :
            if arr[i][j] != arr[j][i] :
                return 0
    return answer


# 0 떼기
# 정수로 이루어진 문자열 n_str이 주어질 때, n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181847
def solution(n_str):
    answer = ''
    for i in n_str :
        if len(answer) > 0 :
            answer += i
        else :
            if i != '0' :
                answer += i
    return answer


# 부분 문자열인지 확인하기
'''부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다. 
예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만, 
"aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.
문자열 my_string과 target이 매개변수로 주어질 때, target이 문자열 my_string의 부분 문자열이라면 1을, 
아니라면 0을 return 하는 solution 함수를 작성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181843
def solution(my_string, target):
    if target in my_string :
        return 1
    return 0


# 정수 찾기
# 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181840
def solution(num_list, n):
    if n in num_list :
        return 1
    return 0


# 주사위 게임 2
'''1부터 6까지 숫자가 적힌 주사위가 세 개 있습니다. 세 주사위를 굴렸을 때 나온 숫자를 각각 a, b, c라고 했을 때 얻는 점수는 다음과 같습니다.
세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.
세 정수 a, b, c가 매개변수로 주어질 때, 얻는 점수를 return 하는 solution 함수를 작성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181930
def solution(a, b, c):
    if a != b and a != c and b != c :
        return a + b + c
    elif a != b or a != c or b != c :
        return (a + b + c) * (a**2 + b**2 + c**2)
    else :
        return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)


# 문자열 정렬하기 (2)
# 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120911
def solution(my_string):
    answer = ''
    my_string = sorted(my_string.lower())
    for i in my_string :
        answer += i
    return answer


# 외계행성의 나이
# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120834
def solution(age):
    answer = ''
    alpha = list(map(chr, range(97, 123)))
    for i in str(age) :
        answer += alpha[int(i)]
    return answer


# 배열 회전시키기
# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120844
def solution(numbers, direction):
    if direction == "right" :
        numbers.insert(0,numbers[len(numbers)-1])
        numbers.pop()
    else :
        numbers.append(numbers[0])
        numbers.remove(numbers[0])
    return numbers


# 369게임
# 머쓱이는 친구들과 369게임을 하고 있습니다. 369게임은 1부터 숫자를 하나씩 대며 3, 6, 9가 들어가는 숫자는 숫자 대신 3, 6, 9의 개수만큼 박수를 치는 게임입니다. 머쓱이가 말해야하는 숫자 order가 매개변수로 주어질 때, 머쓱이가 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120891
def solution(order):
    answer = 0
    for i in str(order) :
        if i in ["3","6","9"] :
            answer += 1
    return answer


# 숫자 찾기
# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120904
def solution(num, k):
    for i in range(0, len(str(num))) :
        if str(k) == str(num)[i] :
            return int(i)+1
    return -1


# 글자 지우기
# 문자열 my_string과 정수 배열 indices가 주어질 때, my_string에서 indices의 원소에 해당하는 인덱스의 글자를 지우고 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181900
def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)) :
        if i not in indices :
            answer += my_string[i]
    return answer


# 중복된 문자 제거
# 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120888
def solution(my_string):
    answer = ''
    for i in my_string :
        if i not in answer :
            answer += i
    return answer


# 세로 읽기
# 문자열 my_string과 두 정수 m, c가 주어집니다. my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들을 문자열로 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181904
def solution(my_string, m, c):
    return my_string[c-1::m]


# 문자열이 몇 번 등장하는지 세기
# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181871
def solution(myString, pat):
    answer = 0
    for i in range(len(myString)) :
        if pat in myString[i:i+len(pat)] :
            answer += 1
    return answer


# [PCCE 기출문제] 2번 / 각도 합치기
'''일반적으로 두 선분이 이루는 각도는 한 바퀴를 360도로 하여 표현합니다. 따라서 각도에 360의 배수를 더하거나 빼더라도 같은 각을 의미합니다. 예를 들면, 30도와 390도는 같은 각도입니다.
주어진 코드는 각도를 나타내는 두 정수 angle1과 angle2가 주어질 때, 이 두 각의 합을 0도 이상 360도 미만으로 출력하는 코드입니다. 코드가 올바르게 작동하도록 한 줄을 수정해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/340206
angle1 = int(input())
angle2 = int(input())

sum_angle = (angle1 + angle2) % 360
print(sum_angle)


# 문자열 잘라서 정렬하기
# 문자열 myString이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요. 단, 빈 문자열은 반환할 배열에 넣지 않습니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/181866
def solution(myString):
    answer = sorted(myString.split('x'))
    for i in answer :
        if "" in answer :
            answer.remove("")
    return answer


# 피자 나눠 먹기 (2)
# 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120815#
def solution(n):
    for i in range(1, n * 6 + 1):
        if (6 * i) % n == 0:
            return i