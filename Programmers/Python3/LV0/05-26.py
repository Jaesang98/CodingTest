# 조건에 맞게 수열 변환하기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181835
def solution(arr, k):
    return [i * k if k % 2 != 0 else i + k for i in arr]


# l로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181834
def solution(myString):
    return "".join([i if i > "l" else "l" for i in myString ])


# 정수 부분
# https://school.programmers.co.kr/learn/courses/30/lessons/181850
def solution(flo):
    return int(flo)


# 숫자 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/120904
def solution(num, k):
    for i,v in enumerate(str(num)) :
        if str(k) == v :
            return i+1
    return -1


# 문자열 바꿔서 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181864
def solution(myString, pat):
    myString = myString.replace("A", "C")
    myString = myString.replace("B", "A")
    myString = myString.replace("C", "B")
    return 1 if pat in myString else 0


# 정수 찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/181840
def solution(num_list, n):
    return 1 if n in num_list else 0


# 배열의 원소 삭제하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181844
def solution(arr, delete_list):
    for i in delete_list :
        if i in arr :
            arr.remove(i)
    return arr


# 꼬리 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181841
def solution(str_list, ex):
    answer = ""
    for i in str_list :
        if ex not in i :
            answer += i
    return answer


# 0 떼기
# https://school.programmers.co.kr/learn/courses/30/lessons/181847
def solution(n_str):
    return n_str.lstrip("0")


# 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/181842
def solution(str1, str2):
    return 1 if str1 in str2 else 0