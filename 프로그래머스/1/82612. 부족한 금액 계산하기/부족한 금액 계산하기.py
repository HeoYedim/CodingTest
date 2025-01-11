def solution(price, money, count):
    total_cost = sum(price * (i + 1) for i in range(count))
    return max(0, total_cost - money)