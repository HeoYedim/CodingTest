def solution(binomial):
    a, op, b = binomial.split()
    
    return {'+': int(a) + int(b), '-': int(a) - int(b), '*': int(a) * int(b)}[op]