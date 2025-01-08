def solution(a, b):
    if a % 2 != b % 2:
        return 2 * (a + b)
    elif a % 2 == 1:
        return a * a + b * b
    else:
        return abs(a - b)