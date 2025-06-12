# 문자 개수 세기
# https://school.programmers.co.kr/learn/courses/30/lessons/181902
def solution(my_string):
    alpha_1 = 'abcdefghijklmnopqrstuvwxyz'
    alpha_2 = alpha_1.upper()
    answer = [0]*52

    for i in my_string:
        if i in alpha_2:
            answer[alpha_2.index(i)] += 1
        else :
            answer[alpha_1.index(i) + 26] += 1
        
    return answer
    
# 이진수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120885
def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]
    

# 소인수분해
# https://school.programmers.co.kr/learn/courses/30/lessons/120852
def solution(n):
    answer = []
    count = 2
    
    while n > 1 :
        if n % count == 0 :
            n = n // count
            answer.append(count)
        else :
            count += 1
            
    answer = list(set(answer))
    answer.sort()
    return answer
        