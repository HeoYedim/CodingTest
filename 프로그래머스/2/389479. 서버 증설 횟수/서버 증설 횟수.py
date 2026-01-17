def solution(players, m, k):
    server = [0] * len(players)
    current_server = 0
    answer = 0
    
    for t in range(len(players)):
        current_server += server[t]
        
        required_server = players[t] // m
        
        if current_server < required_server:
            add = required_server - current_server
            answer += add
            current_server += add
            
            if t + k < len(server):
                server[t + k] -= add
    
    return answer