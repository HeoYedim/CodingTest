def solution(today, terms, privacies):
    answer = []
    type_terms = {}
    date = ""
    validity_term = []
    
    # terms를 dictionary로 만들기 {A : 6,...}
    for term in terms:
        term = term.split()
        type_terms[term[0]] = term[1]
        
    for privacy in privacies:
        privacy = privacy.split(" ")
        # ["2021.05.02", 6]
        privacy[1] = int(type_terms[privacy[1]])
        
        # [2021, 05, 02]
        date = privacy[0].split('.')
        
        year = int(date[0])
        # 5
        month = int(date[1])
        # 2
        day = int(date[2])
        
        month = month + privacy[1]
        
        while month >= 13:
            year += 1
            month = month - 12
        
        # 5 -> 05
        month = str(month).zfill(2)
        day = str(day).zfill(2)
        # ["20220102",,]
        validity_term.append(''.join(map(str, [year, month, day])))
        
    # "20220519"
    today = today.replace(".", "")
            
    for i in range(len(validity_term)):
        if today >= validity_term[i]:
            answer.append(i+1)
            
    return answer
        