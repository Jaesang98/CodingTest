# 문자열 섞기
# https://school.programmers.co.kr/learn/courses/30/lessons/181942
def solution(str1, str2):
    return ''.join([str1[i] + str2[i] for i in range(len(str1))])


# 1로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181880
def solution(num_list):
    answer = 0
    for i in num_list :
        while i > 1 :
            if i % 2 == 0 :
                i = i // 2
                answer += 1
            else :
                i = (i-1) // 2
                answer += 1
    return answer


# 문자열 뒤집기
# https://school.programmers.co.kr/learn/courses/30/lessons/181905
def solution(my_string, s, e):
    return my_string.replace(my_string[s:e+1] , my_string[s:e+1][::-1])


# 모스부호 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120838
def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    
    answer = letter.split()
    return "".join([morse[i] for i in answer])


# 2차원으로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/120842
def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list), n) :
        answer.append(num_list[i : i+n])
    return answer