def solution(s):
    c=[]
    
    for i in s:
        if i == '(':
            c.append(i)
        else:
            if len(c)==0:
                return False
            else:
                c.pop()
                
    if len(c)==0:
        return True
    else:
        return False