def time_sec(time):
    return int(time[0:2])*60 + int(time[3:5])

def solution(video_len, pos, op_start, op_end, commands):
    
    present = time_sec(pos)
    t_op_start = time_sec(op_start)
    t_op_end = time_sec(op_end)
    total = time_sec(video_len)
    
    if t_op_start <= present <= t_op_end:
        present = t_op_end
        
    for command in commands:
        if command == 'next':
            present += 10
            if present > total:
                present = total
                
        else:
            present -= 10
            if present < 10:
                present = 0
                    
        if t_op_start <= present <= t_op_end:
            present = t_op_end
    
    answer = "%02d:%02d" % (int(present / 60), int(present % 60))
    
    return answer