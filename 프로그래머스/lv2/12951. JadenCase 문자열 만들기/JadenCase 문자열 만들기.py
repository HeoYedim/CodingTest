def solution(s):
    answer=[]
    s = s.split(" ")
    
    for sentence in s:
        answer.append(sentence.capitalize())
            
    return ' '.join(answer)