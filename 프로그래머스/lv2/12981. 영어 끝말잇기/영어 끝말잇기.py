def solution(n, words):
    
    for i in range(len(words)-1):
        # 틀린 words의 인덱스는 i+1번째
        if words[i][-1] != words[i+1][0] or words[i+1] in words[:i+1]:
            return [(i+1)%n+1, (i+1)//n+1]
            
    return [0,0]