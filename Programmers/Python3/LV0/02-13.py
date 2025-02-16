# 배열 만들기 3
'''정수 배열 arr와 2개의 구간이 담긴 배열 intervals가 주어집니다.
intervals는 항상 [[a1, b1], [a2, b2]]의 꼴로 주어지며 각 구간은 닫힌 구간입니다. 닫힌 구간은 양 끝값과 그 사이의 값을 모두 포함하는 구간을 의미합니다.
이때 배열 arr의 첫 번째 구간에 해당하는 배열과 두 번째 구간에 해당하는 배열을 앞뒤로 붙여 새로운 배열을 만들어 return 하는 solution 함수를 완성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181895
def solution(arr, intervals):
    return arr[intervals[0][0] : intervals[0][1]+1] + arr[intervals[1][0] : intervals[1][1]+1]


# 합성수 찾기
# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120846
def solution(n):
    answer = 0
    for i in range(1,n+1) :
        count = 0
        for j in range(1,n+1) :
            if count < 3 and i % j == 0 :
                count += 1
        if count > 2 :
            answer +=1
    return answer


# 등차수열의 특정한 항만 더하기
# 두 정수 a, d와 길이가 n인 boolean 배열 included가 주어집니다. 첫째항이 a, 공차가 d인 등차수열에서 included[i]가 i + 1항을 의미할 때, 이 등차수열의 1항부터 n항까지 included가 true인 항들만 더한 값을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181931
def solution(a, d, included):
    answer = 0
    for i in range(len(included)) :
        if i > 0 : a += d
        if included[i] : answer += a
    return answer


# 문자열 섞기
# 길이가 같은 두 문자열 str1과 str2가 주어집니다. 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181942
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)) :
        answer += str1[i] + str2[i]
    return answer


# 모스부호 (1)
# 머쓱이는 친구에게 모스부호를 이용한 편지를 받았습니다. 그냥은 읽을 수 없어 이를 해독하는 프로그램을 만들려고 합니다. 문자열 letter가 매개변수로 주어질 때, letter를 영어 소문자로 바꾼 문자열을 return 하도록 solution 함수를 완성해보세요. 모스부호는 다음과 같습니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/120838
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    answer = ''
    for i in letter.split(' ') :
        answer += morse[i]
    return answer


# 2차원으로 만들기
'''정수 배열 num_list와 정수 n이 매개변수로 주어집니다. num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
num_list가 [1, 2, 3, 4, 5, 6, 7, 8] 로 길이가 8이고 n이 2이므로 num_list를 2 * 4 배열로 다음과 같이 변경합니다. 2차원으로 바꿀 때에는 num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 변경합니다.
'''
# https://school.programmers.co.kr/learn/courses/30/lessons/120842
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n) :
        answer.append(num_list[i: i+n])
    return answer


# 1로 만들기
'''정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.
10 / 2 = 5
(5 - 1) / 2 = 2
2 / 2 = 1
위와 같이 3번의 나누기 연산으로 1이 되었습니다.
정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.
'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181880
def solution(num_list):
    answer = 0
    for i in num_list :
        one = i
        while one != 1 :
            if one % 2 == 0 :
                one = one // 2
            else :
                one = (one-1) // 2
            answer += 1
    return answer


# 문자열 뒤집기
# 문자열 my_string과 정수 s, e가 매개변수로 주어질 때, my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181905
def solution(my_string, s, e):
    answer = ''
    my_string = list(my_string)
    my_string[s:e+1] = list(reversed(my_string[s:e+1]))
    for i in my_string :
        answer += i
    return answer


# 배열 만들기 5
'''문자열 배열 intStrs와 정수 k, s, l가 주어집니다. intStrs의 원소는 숫자로 이루어져 있습니다.
배열 intStrs의 각 원소마다 s번 인덱스에서 시작하는 길이 l짜리 부분 문자열을 잘라내 정수로 변환합니다. 이때 변환한 정수값이 k보다 큰 값들을 담은 배열을 return 하는 solution 함수를 완성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181912
def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs :
        if int(i[s:s+l]) > k :
            answer.append(int(i[s:s+l]))
    return answer


# 수열과 구간 쿼리 3
'''정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [i, j] 꼴입니다.
각 query마다 순서대로 arr[i]의 값과 arr[j]의 값을 서로 바꿉니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181924
def solution(arr, queries):
    answer = ''
    for i in queries :
        answer = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = answer
    return arr


# k의 개수
# 1부터 13까지의 수에서, 1은 1, 10, 11, 12, 13 이렇게 총 6번 등장합니다. 정수 i, j, k가 매개변수로 주어질 때, i부터 j까지 k가 몇 번 등장하는지 return 하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120887
def solution(i, j, k):
    answer = 0
    for a in range(i,j+1) :
        for b in str(a) :
            if str(k) in b :
                answer += 1
    return answer


# 팩토리얼
# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120848
def solution(n):
    answer = 1
    for i in range(1,11) :
        answer *= i
        if answer == n :
            return i
        elif answer > n :
            return i -1


# 숨어있는 숫자의 덧셈 (2)
# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120848
def solution(my_string):
    answer = ''
    answer2 = 0
    for i in my_string :
        if i.isdigit() :
            answer += i
        else :
            answer += 'a'
    
    for j in answer.split('a') :
        if j != "" :
            answer2 += int(j)
    return answer2


# 날짜 비교하기
# 정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다. 만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181838
def solution(date1, date2):
    if date1[0] < date2[0] :
        return 1
    elif date1[0] == date2[0] :
        if date1[1] < date2[1] :
            return 1
        elif date1[1] == date2[1] :
            if date1[2] < date2[2] :
                return 1
            else :
                return 0
        else :
            return 0
    else :
        return 0


# 수열과 구간 쿼리 1
'''정수 배열 arr와 2차원 정수 배열 queries이 주어집니다. queries의 원소는 각각 하나의 query를 나타내며, [s, e] 꼴입니다.
각 query마다 순서대로 s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.
위 규칙에 따라 queries를 처리한 이후의 arr를 return 하는 solution 함수를 완성해 주세요.'''
# https://school.programmers.co.kr/learn/courses/30/lessons/181883
def solution(arr, queries):
    for i in queries :
        for j in range(i[0], i[1]+1):
            arr[j] += 1
    return arr


# A로 B 만들기
# 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120886
def solution(before, after):
    for i in before :
        if before.count(i) != after.count(i) :
            return 0
    return 1


# 이차원 배열 대각선 순회하기
# 2차원 정수 배열 board와 정수 k가 주어집니다. i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는 solution 함수를 완성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181829
def solution(board, k):
    answer = 0
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if i + j <= k :
                answer += board[i][j]
    return answer


# 한 번만 등장한 문자
# 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.
# https://school.programmers.co.kr/learn/courses/30/lessons/120896
def solution(s):
    s = sorted(s)
    for i in s[:] :
        if s.count(i) > 1:
            while i in s :
                s.remove(i)
    return "".join(s)


# 가까운 수
# 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/120890
def solution(array, n):
    answer = 0
    array2 = []
    array3 = []
    for i in range(len(array)) :
        array2.append(array[i])
        array[i] = abs(array[i] - n)
        
    if array.count(min(array)) > 1 :
        for j in range(len(array)) :
            if array[j] == min(array):
                array3.append(array2[j])
        return min(array3)
    else :
        return array2[array.index(min(array))]


# 배열의 길이를 2의 거듭제곱으로 만들기
# 정수 배열 arr이 매개변수로 주어집니다. arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다. arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/181857
def solution(arr):
    two = 0
    for i in range(0,11) :
        if 2**i >= len(arr) :
            two = 2**i
            break
    while two != len(arr) :
        arr.append(0)
    return arr