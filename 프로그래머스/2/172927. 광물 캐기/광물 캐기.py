def solution(picks, minerals):
    answer = 0
    # 캘 광물 개수
    max_mineral = sum(picks) * 5
    minerals = minerals[:max_mineral]
    
    # 5개씩 끊어
    minerals_group = []
    for i in range(0, len(minerals), 5):
        group = minerals[i:i+5]
        
        dia = group.count("diamond")
        iron = group.count("iron")
        st = group.count("stone")
        
        score = dia * 25 + iron * 5 + st * 1
        minerals_group.append((score, dia, iron, st))
    
    #  [(13, 3, 2, 0), (5, 1, 1, 0)]
    minerals_group.sort(reverse=True)
    
    for score, dia, iron, st in minerals_group:
        if picks[0] > 0:
            picks[0] -= 1
            answer += dia * 1 + iron * 1 + st * 1
        elif picks[1] > 0:
            picks[1] -= 1
            answer += dia * 5 + iron * 1 + st * 1
        elif picks[2] > 0:
            picks[2] -= 1
            answer += dia * 25 + iron * 5 + st * 1
    return answer