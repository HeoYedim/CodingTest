def solution(k, score):
    answer = []
    last = 0
    honor = []
    
    for i in score:
        if len(honor) < k:
            honor.append(i)
        else:
            if min(honor) <= i:
                honor.remove(min(honor))
                honor.append(i)
                
        last = min(honor)
        answer.append(last)
        
    return answer