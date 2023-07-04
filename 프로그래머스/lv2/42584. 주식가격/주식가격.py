from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while len(queue)>0:
        cnt = 0
        out = queue.popleft()
        
        for i in queue:
            cnt += 1
            if out > i:
                break
        
        answer.append(cnt)
        
    return answer