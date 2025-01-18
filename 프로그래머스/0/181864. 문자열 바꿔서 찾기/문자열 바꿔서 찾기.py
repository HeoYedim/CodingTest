def solution(myString, pat):
    new = ''.join('B' if i == 'A' else 'A' for i in myString)
    return 1 if pat in new else 0