def solution(keymap, targets):
    answer = []
    abc_dict={}
    
    for key in keymap:
        for abc in key:
            if abc not in abc_dict:
                abc_dict[abc]=key.index(abc)+1
            else:
                if abc_dict.get(abc) > key.index(abc)+1:
                    abc_dict[abc]=key.index(abc)+1
                    
    for target in targets:
        tmp=[]
        for t in target:
            if t in abc_dict:
                tmp.append(abc_dict.get(t))
            else:
                tmp.append(-1)
        if -1 in tmp:
            answer.append(-1)
        else:
            answer.append(sum(tmp))
    
    return answer