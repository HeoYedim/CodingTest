def solution(order):
    price = 0
    
    for m in order:
        if "americano" in m or m == "anything":
            price += 4500
        elif "cafelatte" in m:
            price += 5000
            
    return price