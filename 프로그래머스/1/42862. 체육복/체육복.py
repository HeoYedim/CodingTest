def solution(n, lost, reserve):
    real_lost = list(set(lost) - set(reserve))
    real_reserve = list(set(reserve) - set(lost))
    
    for r in (real_reserve):
        if r - 1 in real_lost:
            real_lost.remove(r - 1)
        elif r + 1 in real_lost:
            real_lost.remove(r + 1)
            
    return n - len(real_lost)