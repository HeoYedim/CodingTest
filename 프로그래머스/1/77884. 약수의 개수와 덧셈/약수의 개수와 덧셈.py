def solution(left, right):
    # 약수 개수가 홀수 == 완전제곱수
    # 완전제곱수 판별 : (i ** 0.5) % 1 == 0
    return sum(i if (i ** 0.5) % 1 else -i for i in range(left, right + 1))