def solution(schedules, timelogs, startday):
    def time_minutes(t):
        return (t // 100) * 60 + (t % 100)
    
    answer = 0
    
    for i in range(len(schedules)):
        ok = True
        day = startday
        
        for j in timelogs[i]:
            if ((day - 1) % 7) + 1 not in [6, 7]:
                if time_minutes(j) > time_minutes(schedules[i]) + 10:
                    ok = False
                    break
                    
            day += 1
            
        if ok: answer += 1
                    
    return answer