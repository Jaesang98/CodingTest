# 두 수의 연산값 비교하기
''' 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.
단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.
'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181938
def solution(a, b):
    if int(str(a) + str(b)) > 2 * a * b :
        return int(str(a) + str(b))
    else : 
        return 2 * a * b


# 더 크게 합치기
''' 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.
12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 b ⊕ a 중 더 큰 값을 return 하는 solution 함수를 완성해 주세요.
단, a ⊕ b와 b ⊕ a가 같다면 a ⊕ b를 return 합니다.
'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181939
def solution(a, b):
    if int(str(a) + str(b)) > int(str(b) + str(a)) :
        return int(str(a) + str(b))
    else :
        return int(str(b) + str(a))


# 문자열 곱하기
# 문자열 my_string과 정수 k가 주어질 때, my_string을 k번 반복한 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181940
def solution(my_string, k):
    return my_string * k


# 정수 부분
# 실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181850
def solution(flo):
    return int(flo)


# 뒤에서 5등 위로
# 정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 제외한 수들을 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181852
def solution(num_list):
    num_list.sort()
    return num_list[5:]


# 뒤에서 5등까지
# 정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181853
def solution(num_list):
    num_list.sort()
    return num_list[0:5]


# 배열의 길이에 따라 다른 연산하기
# 정수 배열 arr과 정수 n이 매개변수로 주어집니다. arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181854
def solution(arr, n):
    answer = arr
    if len(arr) % 2 == 0:
        for i in range(1,len(arr),2) :
            answer[i] += n
    else :
        for i in range(0,len(arr),2) :
            answer[i] += n
    return answer


# 배열 비교하기
''' 이 문제에서 두 정수 배열의 대소관계를 다음과 같이 정의합니다.
두 배열의 길이가 다르다면, 배열의 길이가 긴 쪽이 더 큽니다.
배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 다르다면 더 큰 쪽이 크고, 같다면 같습니다.
두 정수 배열 arr1과 arr2가 주어질 때, 위에서 정의한 배열의 대소관계에 대하여 arr2가 크다면 -1, arr1이 크다면 1, 두 배열이 같다면 0을 return 하는 solution 함수를 작성해 주세요.
'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181856
def solution(arr1, arr2):
    if len(arr1) < len(arr2) :
        return -1
    elif len(arr1) > len(arr2) :
        return 1
    else :
        if sum(arr1) > sum(arr2) :
            return 1
        elif sum(arr1) < sum(arr2) :
            return -1
        else :
            return 0


# 배열의 원소만큼 추가하기
# 아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 양의 정수 배열 arr가 매개변수로 주어질 때, arr의 앞에서부터 차례대로 원소를 보면서 원소가 a라면 X의 맨 뒤에 a를 a번 추가하는 일을 반복한 뒤의 배열 X를 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181861
def solution(arr):
    answer = []
    for i in arr :
        for j in range(0,i) :
            answer.append(i)
    return answer


# rny_string
# 'm'과 "rn"이 모양이 비슷하게 생긴 점을 활용해 문자열에 장난을 하려고 합니다. 문자열 rny_string이 주어질 때, rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181863
def solution(rny_string):
    return rny_string.replace('m','rn')


# 문자열 바꿔서 찾기
# 문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181864
def solution(myString, pat):
    answer = 0
    myString2 = ''
    for i in range(0,len(myString)) :
        if myString[i] == 'A' :
            myString2 += 'B'
        elif myString[i] == 'B' :
            myString2 += 'A'
    
    if pat in myString2 :
        answer = 1

    return answer


# 공백으로 구분하기 2
# 단어가 공백 한 개 이상으로 구분되어 있는 문자열 my_string이 매개변수로 주어질 때, my_string에 나온 단어를 앞에서부터 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181868
def solution(my_string):
    return my_string.split()


# ad 제거하기
# 문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181870
def solution(strArr):
    answer = []
    for i in strArr :
        if 'ad' not in i :
            answer.append(i)
    return answer


# 특정한 문자를 대문자로 바꾸기
# 영소문자로 이루어진 문자열 my_string과 영소문자 1글자로 이루어진 문자열 alp가 매개변수로 주어질 때, my_string에서 alp에 해당하는 모든 글자를 대문자로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181873
def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())


# A 강조하기
# 문자열 myString이 주어집니다. myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고, "A"가 아닌 모든 대문자 알파벳은 소문자 알파벳으로 변환하여 return 하는 solution 함수를 완성하세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181874
def solution(myString):
    return myString.lower().replace('a', 'A')


# 배열에서 문자열 대소문자 변환하기
# 문자열 배열 strArr가 주어집니다. 모든 원소가 알파벳으로만 이루어져 있을 때, 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 짝수번째 인덱스의 문자열은 모든 문자를 소문자로 바꿔서 반환하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181875
def solution(strArr):
    answer = []
    for i in range(len(strArr)) :
        if i % 2 == 0 :
            answer.append(strArr[i].lower())
        else :
            answer.append(strArr[i].upper())
    return answer


# 소문자로 바꾸기
# 알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181876
def solution(myString):
    return myString.lower()


# 대문자로 바꾸기
# 알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 대문자로 변환하여 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181877
def solution(myString):
    return myString.upper()


# 원하는 문자열 찾기
# 알파벳으로 이루어진 문자열 myString과 pat이 주어집니다. myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0을 return 하는 solution 함수를 완성해 주세요.단, 알파벳 대문자와 소문자는 구분하지 않습니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/181878
def solution(myString, pat):
    answer = 0
    if pat.lower() in myString.lower() :
        return 1
    return answer


# 길이에 따른 연산
# 정수가 담긴 리스트 num_list가 주어질 때, 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을 10 이하이면 모든 원소의 곱을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181879
def solution(num_list):
    answer = 1
    if len(num_list) > 10 :
        return sum(num_list)
    else :
        for i in num_list :
           answer *= i
    return answer