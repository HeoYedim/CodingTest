from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    cases = [10, 20, 30, 40]
    
    # 완전탐색 => case=(10, 10, 10, 10), (10, 10, 10, 20) ...
    for case in product(cases, repeat=len(emoticons)):
        total_paid, emoticon_plus = 0, 0
        
        for rate, max_price in users:
            paid = 0
            for i, emoticon in enumerate(emoticons):
                # 임티 할인률 >= rate -> 구매
                if case[i] >= rate: 
                    paid += emoticon * (100 - case[i]) // 100
            # 임티 구매 취소 후 플러스 가입
            if paid >= max_price:
                emoticon_plus += 1
            else:
                total_paid += paid
        
        # 플러스 가입자 수 증가
        if emoticon_plus > answer[0]:
            answer[0], answer[1] = emoticon_plus, total_paid
        elif emoticon_plus == answer[0] and total_paid > answer[1]:
            answer[1] = total_paid
    
    return answer