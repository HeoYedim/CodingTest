def solution(n, control):
    ctl = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    
    return n + sum(ctl[i] for i in control)