import sys

N, M = map(int, sys.stdin.readline().split())
basket = [0] * N

for _ in range(M):
    start, end, ball = map(int, sys.stdin.readline().split())
    for i in range(start - 1, end):
        basket[i] = ball

print(" ".join(map(str, basket)))