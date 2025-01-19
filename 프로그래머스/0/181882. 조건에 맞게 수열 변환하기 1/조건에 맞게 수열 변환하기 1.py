def transform(i):
    if i >= 50 and i % 2 == 0:
        return i // 2
    elif i < 50 and i % 2 != 0:
        return i * 2
    return i

def solution(arr):
    return [transform(i) for i in arr]