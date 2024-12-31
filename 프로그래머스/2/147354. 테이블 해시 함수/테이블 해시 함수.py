def solution(data, col, row_begin, row_end):
    answer = 0
    # 1. data 정렬
    data = sorted(data, key = lambda x: (x[col - 1], -x[0]))
    
    # 2. S_i 누적
    for i in range(row_begin, row_end + 1):
        s_i = 0
        for j in data[i - 1]:
            s_i += j % i
            
        answer ^= s_i
    return answer