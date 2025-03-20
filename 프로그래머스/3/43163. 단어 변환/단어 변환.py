from collections import deque

def difference(word1, word2):
    return sum(1 for a, b in zip(word1, word2) if a != b) == 1

def solution(begin, target, words):
    visited = [False] * len(words)
    queue = deque([(begin, 0)])
    
    while queue:
        current, count = queue.popleft()
        
        if current == target:
            return count
        
        for idx in range(len(words)):
            if not visited[idx] and difference(current, words[idx]):
                queue.append((words[idx], count + 1))
                visited[idx] = True
    
    return 0