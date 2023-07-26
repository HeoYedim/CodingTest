def solution(s):
    answer = []
    index_dict = {}
    
    for i in range(len(s)):
        if s[i] not in index_dict:
            answer.append(-1)
        else:
            answer.append(i-index_dict[s[i]])
        index_dict[s[i]]=i
    return answer