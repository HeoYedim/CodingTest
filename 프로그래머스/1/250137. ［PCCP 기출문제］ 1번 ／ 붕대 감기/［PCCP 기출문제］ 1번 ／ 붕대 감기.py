def solution(bandage, health, attacks):
    answer = health
    skill = 0 # 회복 연속 성공
    timeline = 1
    
    while len(attacks) > 0:
        # 공격 시간일 때
        if attacks[0][0] == timeline:
            skill = 0
            answer -= attacks[0][1]
            attacks.pop(0)
            if answer <= 0:
                answer = -1
                break
            
        # 공격 시간 아닐 때
        else:
            skill += 1
            if skill == bandage[0]:
                answer += bandage[2] + bandage[1]
                skill = 0
            else:
                answer += bandage[1]
                
            if answer > health:
                answer = health
        timeline += 1
    
    return answer