# 모의고사
# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 완전탐색
def solution(answers):
    answer_dict = {"one" : 0, "two" : 0, "three" : 0,}
    max_value = 0
    answer = []
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)) :
        if one[i % len(one)] == answers[i] :
            answer_dict["one"] += 1
            
        if two[i % len(two)] == answers[i] :
            answer_dict["two"] += 1
            
        if three[i % len(three)] == answers[i] :
            answer_dict["three"] += 1
            
    max_value = max(answer_dict.values())
    for key in answer_dict :
        if answer_dict[key] == max_value :
            if key == "one" :
                answer.append(1)
            elif key == "two" :
                answer.append(2)
            else :
                answer.append(3)
    
    return answer
