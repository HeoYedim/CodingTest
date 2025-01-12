def solution(numbers, hand):
    answer = ''
    
    xy = { 1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
          4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
          7 : [2, 0], 8 : [2, 1], 9 : [2, 2],
          '*' : [3, 0], 0 : [3, 1], '#' : [3, 2]}
    
    LEFT = xy['*']
    RIGHT = xy['#']
    
    for i in numbers:
        num = xy[i]
        
        if i in [1, 4, 7]:
            answer += 'L'
            LEFT = num
        elif i in [3, 6, 9]:
            answer += 'R'
            RIGHT = num
            
        else:
            LEFT_d = 0
            RIGHT_d = 0
            
            for a, b, c in zip(LEFT, RIGHT, num):
                LEFT_d += abs(a-c)
                RIGHT_d += abs(b-c)
            
            if LEFT_d < RIGHT_d:
                answer += 'L'
                LEFT = num
            elif LEFT_d > RIGHT_d:
                answer += 'R'
                RIGHT = num
            else:
                if hand == 'left':
                    answer += 'L'
                    LEFT = num
                else:
                    answer += "R"
                    RIGHT = num
                    
    return answer