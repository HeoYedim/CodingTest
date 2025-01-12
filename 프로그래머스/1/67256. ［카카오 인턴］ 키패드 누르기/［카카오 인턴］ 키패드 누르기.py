def solution(numbers, hand):
    answer = ''
    
    num_dict = {'*' : 10, "0" : 11, '#' : 12}
    
    LEFT = num_dict('*')
    RIGHT = num_dict('#')
    
    for num in numbers:
        if str(num) in ["1", "4", "7", '*']:
            answer+="L"
            LEFT = num
        elif str(num) in ["3", "6", "9", '#']:
            answer+="R"
            RIGHT = num
        
        if str(num) in ["2", "5", "8", "0"]:
            if (abs(int(LEFT) - int(num)) // 3) + (abs(int(LEFT) - int(num)) % 3) < (abs(int(RIGHT) - int(num)) // 3) + (abs(int(RIGHT) - int(num)) % 3):
                answer += "L"
                LEFT = num
            elif (abs(int(LEFT) - int(num)) // 3) + (abs(int(LEFT) - int(num)) % 3) > (abs(int(RIGHT) - int(num)) // 3) + (abs(int(RIGHT) - int(num)) % 3):
                answer += "R"
                RIGHT = num
            else :
                if hand == "right" :
                    answer += "R"
                    RIGHT = num
                else:
                    answer += "L"
                    LEFT = num
                    
    return answer