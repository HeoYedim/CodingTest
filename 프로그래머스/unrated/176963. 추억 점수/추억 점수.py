def solution(name, yearning, photo):
    answer = []
    score_dict = {}
    score = 0
    
    for i in range(len(name)):
        score_dict[name[i]]=yearning[i]
        
    for people in photo:
        for person in people:
            if person in score_dict:
                score+=score_dict.get(person)
        answer.append(score)
        score=0
    
    return answer