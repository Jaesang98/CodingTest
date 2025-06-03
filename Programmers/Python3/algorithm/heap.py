# 더 맵게
# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# heap
import heapq
def solution(scoville, K):
    one = 0
    two = 0
    count = 0
    heapq.heapify(scoville)
    
    while scoville and scoville[0] < K :
        
        if len(scoville) < 2 :
            return -1
        
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        if one >= K : break
        heapq.heappush(scoville, one + (two*2))
        count += 1
    return count