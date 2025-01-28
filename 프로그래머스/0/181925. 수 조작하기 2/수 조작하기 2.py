def solution(numLog):
    diff = {1: 'w', -1: "s", 10: "d", -10: "a"}
    return ''.join(diff[numLog[i + 1] - numLog[i]] for i in range(len(numLog) - 1))