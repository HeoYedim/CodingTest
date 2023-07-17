def solution(sizes):
    answer = []
    s_max = 0
    s_min = 0
    
    for i in sizes:
        answer.append([max(i), min(i)])
        if s_max< max(i): s_max=max(i)
        if s_min< min(i): s_min=min(i)
        
    return s_max*s_min