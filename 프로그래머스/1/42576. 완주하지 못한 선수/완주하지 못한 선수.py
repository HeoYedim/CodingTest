from collections import Counter

def solution(participant, completion):
    hash = Counter(participant) - Counter(completion)
    return list(hash.keys())[0]