# 컨트롤 제트
# https://school.programmers.co.kr/learn/courses/30/lessons/120853
def solution(s):
    answer = 0
    s = s.split()
    
    for i in range(len(s)) :
        if i == 0 and s[i] == "Z":
            continue
        elif s[i] == "Z" :
            answer -= int(s[i-1])
        else :
            answer += int(s[i])
        
    return answer


# 문자열 반복해서 출력하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181950
str, n = input().strip().split(' ')
n = int(n)
print(str * n)


# 리스트 자르기
# https://school.programmers.co.kr/learn/courses/30/lessons/181897
def solution(n, slicer, num_list):
    if n == 1 :
        return num_list[:slicer[1]+1]
    elif n == 2 :
        return num_list[slicer[0]:]
    elif n == 3 :
        return num_list[slicer[0]:slicer[1]+1]
    else :
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]


# 수열과 구간 쿼리 4
# https://school.programmers.co.kr/learn/courses/30/lessons/181922
def solution(arr, queries):
    for i in queries :
        for j in range(i[0], i[1]+1) :
            if j % i[2] == 0 :
                arr[j] += 1
    return arr


# 2의 영역
# https://school.programmers.co.kr/learn/courses/30/lessons/181894
def solution(arr):
    first = 0
    second = 0
    
    for i in range(len(arr)) :
        if arr[i] == 2 :
            first = i
            break
            
    for i in range(len(arr)-1,0,-1) :
        if arr[i] == 2 :
            second = i
            break
    
    if first == 0 and second == 0 :
        return [-1]
    else :
        return arr[first : second+1]