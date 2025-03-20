def solution(brown, yellow):
    answer = []
    divisors = []
    
    for i in range(1, int(yellow**0.5) + 1):
        if yellow % i == 0:
            divisors.append((i, yellow // i))
            
    for j in range(len(divisors)):
        if 2 * sum(divisors[j]) + 4 == brown:
            answer.append(divisors[j][1] + 2)
            answer.append(divisors[j][0] + 2)
    
    return answer