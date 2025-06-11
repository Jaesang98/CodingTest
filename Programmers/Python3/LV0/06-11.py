# 커피 심부름
# https://school.programmers.co.kr/learn/courses/30/lessons/181837
def solution(order):
    answer = 0
    for i in order :
        if "americano" in i or "anything" == i :
            answer += 4500
        else :
            answer += 5000
    return answer


# 잘라서 배열로 저장하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120913
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n) :
        answer.append(my_str[i:n+i])
    return answer


# 특수문자 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181948
print('!@#$%^&*(\\\'"<>?:;')


# qr code
# https://school.programmers.co.kr/learn/courses/30/lessons/181903
def solution(q, r, code):
    return "".join([code[i] for i in range(len(code)) if i%q == r])


# 조건에 맞게 수열 변환하기 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181881
def solution(arr):
    count = 0
    answer = []
    while True :
        answer = [i for i in arr]
        
        for i in range(len(arr)) :
            if arr[i] > 50 and arr[i] % 2 == 0 :
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 != 0 :
                arr[i] = arr[i]*2 + 1
                
        if answer == arr :
            return count
        
        count += 1