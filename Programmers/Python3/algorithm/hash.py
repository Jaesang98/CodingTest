# 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# hash
def solution(participant, completion):
    answer_list = participant + completion
    answer_dict = {}
    
    for i in answer_list :
        if i not in answer_dict :
            answer_dict[i] = 1
        else :
            answer_dict[i] += 1
            
    for key in answer_dict :
        if answer_dict[key] % 2 != 0  :
            return key

## GPT답변: 이게더 깔끔한듯
def solution(participant, completion):
    hash_dict = {}

    for p in participant:
        hash_dict[p] = hash_dict.get(p, 0) + 1

    for c in completion:
        hash_dict[c] -= 1

    for key, value in hash_dict.items():
        if value > 0:
            return key



# 폰켓몬
# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# hash
def solution(nums):
    hash_dict = {}
    answer = []
    for i in nums :
        hash_dict[i] = hash_dict.get(i,0) + 1
        
    for key in hash_dict :
        answer.append(key)
        
    if len(nums) // 2 < len(answer) :
        return len(nums) // 2
    else :
        return len(answer)