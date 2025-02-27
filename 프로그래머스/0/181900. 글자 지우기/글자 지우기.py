def solution(my_string, indices):
    result = list(my_string)
    
    for idx in sorted(indices, reverse=True):
        del result[idx]
    
    return ''.join(result)