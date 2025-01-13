def game_simulation(diffs, times, limit, level):
    time_required = 0
    
    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        time_prev = times[i-1]
        
        if diff < level:
            time_required += time_cur
        else:
            game_fail = diff - level
            time_required += (time_cur + time_prev) * game_fail + time_cur

        if time_required > limit :
            return False
        
    return True

def solution(diffs, times, limit):
    low = 1
    high = max(diffs)
    
    while low <= high:
        mid_level = (low + high) // 2
        result = game_simulation(diffs, times, limit, mid_level)
        
        if result:
            high = mid_level - 1

        else: 
            low = mid_level + 1

    return low