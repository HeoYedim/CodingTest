def solution(survey, choices):
    answer = ''
    type_dict = {"R": 0,"T": 0,"C": 0,"F": 0,"J": 0,"M": 0,"A": 0,"N": 0}
    
    for i in range(len(choices)):
        if choices[i] < 4:
            type_dict[survey[i][0]] += 4-choices[i]
        elif choices[i] > 4:
            type_dict[survey[i][1]] += choices[i]-4
            
    
    answer+="R" if type_dict["R"] >= type_dict["T"] else "T"
    answer+="C" if type_dict["C"] >= type_dict["F"] else "F"
    answer+="J" if type_dict["J"] >= type_dict["M"] else "M"
    answer+="A" if type_dict["A"] >= type_dict["N"] else "N"
    
    return answer
            