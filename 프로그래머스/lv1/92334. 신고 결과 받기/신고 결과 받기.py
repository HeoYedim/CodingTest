def solution(id_list, report, k):
    answer = []
    report = set(report)
    report_dict = {}
    report_values = []
    report_k = []
    
    # report_dict={"frodo":["neo"],"apeach":["muzi","frodo"],"muzi":["neo","frodo"]}
    for i in report:
        id = i.split(" ")
        if id[0] in report_dict:
            report_dict[id[0]]+=[id[1]]
        else:
            report_dict[id[0]]=[id[1]]
            
    # report_values=["neo","frodo","frodo","muzi","neo"]
    for j in report_dict.values():
        report_values += j
        
    # 정지된 유저 및 횟수 리스트 ["frodo", "neo"]
    for c in id_list:
        if report_values.count(c)>=k:
            report_k+=[c]
            
    for user in id_list:
        cnt=0
        if user in report_dict.keys():
            for i in report_dict[user]:
                if i in report_k:
                    cnt+=1
        answer+=[cnt]
            
    return answer