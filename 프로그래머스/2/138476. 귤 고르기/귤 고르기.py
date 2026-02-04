from collections import Counter
def solution(k, tangerine):
    c = Counter(tangerine)
    counts = sorted(c.values(), reverse=True)
    
    total = 0
    answer = 0
    
    for count in counts:
        total += count
        answer += 1
        if total >= k:
            break
    
    return answer