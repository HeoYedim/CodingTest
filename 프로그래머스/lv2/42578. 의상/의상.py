def solution(clothes):
    clothes_dict = {}
    answer = 1
    
    for c in clothes:
        if c[1] not in clothes_dict.keys():
            clothes_dict[c[1]] = [c[0]]
        else:
            clothes_dict[c[1]].append(c[0])
            
    for c_value in clothes_dict.values():
        answer *= len(c_value)+1
            
    return answer-1