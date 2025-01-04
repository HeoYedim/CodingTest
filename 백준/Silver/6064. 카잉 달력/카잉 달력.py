import sys

def calculate(m, n, x, y):
    k = x # k번째 해
    
    while k <= m * n:
        # (k-x)는 m의 배수, (k-y)는 n의 배수
        if (k - x) % m == 0 and (k - y) % n == 0:
            return k
        k += m
    return -1

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    
    print(calculate(M, N, x, y))