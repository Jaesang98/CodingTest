# A로 B 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120886
def solution(before, after):
    for i in before :
        if before.count(i) != after.count(i) :
            return 0
    return 1


# k의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/120887
def solution(i, j, k):
    answer = 0
    for a in range(i, j+1) :
        if str(k) in str(a) :
            answer += str(a).count(str(k))
            
    return answer


# 문자열이 몇 번 등장하는지 세기
# https://school.programmers.co.kr/learn/courses/30/lessons/181871
def solution(myString, pat):
    answer = 0
    for i in range(len(myString) - len(pat) + 1) :
        if pat == myString[i : i+len(pat)] :
            answer += 1
    return answer


# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181872
def solution(myString, pat):
    for i in range(len(myString)) :
        if pat in myString[len(myString) - len(pat) - i : len(myString) - i] :
            return myString[:len(myString) - i]


# 배열의 길이를 2의 거듭제곱으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181857
def solution(arr):
    count = 0
    while 1 :
        if 2 ** count == len(arr) :
            break
        elif 2 ** count < len(arr) :
            count += 1
        else :
            arr.append(0)
    return arr