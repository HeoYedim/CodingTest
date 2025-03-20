def solution(name):
    answer = 0
    move = len(name) - 1
    
    for idx, char in enumerate(name):
        answer += min(ord(char) - ord('A'), 26 - (ord(char) - ord('A')))
        
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
            
        move = min(move, 2 * idx + (len(name) - next_idx), idx + 2 * (len(name) - next_idx))
        
    answer += move
    
    return answer