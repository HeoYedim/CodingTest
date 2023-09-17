def solution(id_list, report, k):
    report=set(report)
    mail_cnt={x: 0 for x in id_list}
    report_dict = {x: 0 for x in id_list}
    
    for x in report:
        report_dict[x.split()[1]]+=1
        
    for x in report:
        if report_dict[x.split()[1]] >= k:
            mail_cnt[x.split()[0]] +=1
            
    return list(mail_cnt.values())