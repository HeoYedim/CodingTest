def solution(num_list):
    even, odd = '', ''
    
    # 윌러스 연산자 :=
    for i in num_list:
        (even := even + str(i)) if i % 2 == 0 else (odd := odd + str(i))
        
    return int(even) + int(odd)