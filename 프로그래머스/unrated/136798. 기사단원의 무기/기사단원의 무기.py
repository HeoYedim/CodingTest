def solution(number, limit, power):
    answer = 1
    
    for num in range(2, number+1):
        divisor = 0
        
        for i in range(1, int(num**(1/2)+1)):
            if num%i==0:
                divisor+=1
                if i**2!=num:
                    divisor+=1
            
        answer+=divisor if divisor<=limit else power 
            
    return answer
    