from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    days = deque()
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
    
    while days:
        finish = days.popleft()
        count = 1
        
        while days and finish >= days[0]:
            days.popleft()
            count += 1
            
        answer.append(count)
        
    return answer