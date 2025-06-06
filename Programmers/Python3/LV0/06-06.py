# 수열과 구간 쿼리 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181924
def solution(arr, queries):
    for i in queries :
        arr[i[0]], arr[i[1]] = arr[i[1]], arr[i[0]] 
    return arr


# 문자열 묶기
# https://school.programmers.co.kr/learn/courses/30/lessons/181855
def solution(strArr):
    answer_dict = {}
    for i in strArr :
        answer_dict[len(i)] = answer_dict.get(len(i), 0) + 1
    return max(answer_dict.values())


# 세 개의 구분자
# https://school.programmers.co.kr/learn/courses/30/lessons/181862
def solution(myStr):
    myStr = myStr.replace('b', "a")
    myStr = myStr.replace('c', "a")
    myStr = myStr.split("a")
    mySrt = [i for i in myStr if i]
    return mySrt if len(mySrt) > 0 else ["EMPTY"]


# 한 번만 등장한 문자
# https://school.programmers.co.kr/learn/courses/30/lessons/120896
def solution(s):
    answer_dict = {}
    answer = ""
    for i in s :
        answer_dict[i] = answer_dict.get(i,0) + 1
        
    for key in sorted(answer_dict) :
        if answer_dict[key] == 1 :
            answer += key

    return answer


# 간단한 논리 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/181917
def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)