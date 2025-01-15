from collections import deque

def solution(cards1, cards2, goal):
    goal, cards1, cards2 = deque(goal), deque(cards1), deque(cards2)
    
    while goal:
        word = goal.popleft()
        
        if cards1 and cards1[0] == word:
            cards1.popleft()
        elif cards2 and cards2[0] == word:
            cards2.popleft()
        else:
            return "No"
    return "Yes"