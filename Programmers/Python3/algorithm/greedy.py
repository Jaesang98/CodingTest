# 체육복
# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# Greedy
def solution(n, lost, reserve):
    real_lost = [i for i in lost if i not in reserve]
    real_lost.sort()
    real_reserve = [i for i in reserve if i not in lost]
    real_reserve.sort()
    
    answer = n - len(real_lost)
    
    for i in real_lost :
        if i - 1 in real_reserve :
            answer += 1 
            real_reserve.remove(i-1)
        elif i + 1 in real_reserve :
            answer += 1 
            real_reserve.remove(i+1) 
            
    return answer