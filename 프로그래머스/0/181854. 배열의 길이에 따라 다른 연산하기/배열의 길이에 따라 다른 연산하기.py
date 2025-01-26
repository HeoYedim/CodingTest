def solution(arr, n):
    is_even = len(arr) % 2 == 0
    
    for i in range(len(arr)):
        if (is_even and i % 2 != 0) or (not is_even and i % 2 == 0):
            arr[i] += n
    
    return arr