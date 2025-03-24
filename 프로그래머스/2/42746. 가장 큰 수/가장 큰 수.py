def solution(numbers):
    numbers.sort(key = lambda x: str(x) * 10, reverse = True)
    
    return str(int(''.join(map(str, numbers))))