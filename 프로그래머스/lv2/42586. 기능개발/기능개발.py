import math

def solution(progresses, speeds):
    
    answer = []
    finish = [math.ceil((100-progresses[i]) / speeds[i]) for i in range(len(progresses))]
    
    while len(finish)>0:
        
        out = finish.pop(0)
        cnt = 1
        check = finish.copy()
        
        for i in range(len(finish)):
            if out>=finish[i]:
                cnt+=1
                check.pop(0)
            else:
                break
        
        answer.append(cnt)
        finish = check[:]
    
    return answer