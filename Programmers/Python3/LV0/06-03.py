# 세로 읽기
# https://school.programmers.co.kr/learn/courses/30/lessons/181904
def solution(my_string, m, c):
    return my_string[c-1::m]


# 수열과 구간 쿼리 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181883
def solution(arr, queries):
    for i in queries :
        for j in range(i[0], i[1] +1) :
            arr[j] +=1
    return arr


# 빈 배열에 추가, 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181860
def solution(arr, flag):
    answer = []
    for i in range(len(flag)) :
        if flag[i] :
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else :
            for j in range(arr[i]):
                answer.pop()
    return answer


# 날짜 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181838
def solution(date1, date2):
    return 0 if date1 > date2 or date1 == date2 else 1


# 합성수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120846
def solution(n):
    answer = 0
    
    for i in range(1, n+1) :
        count = 0
        for j in range(1, i+1) :
            if i % j == 0 :
                count += 1
        if count >= 3 :
            answer += 1
    return answer