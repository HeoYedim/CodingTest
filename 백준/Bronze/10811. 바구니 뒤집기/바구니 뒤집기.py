import sys

N, M = map(int, sys.stdin.readline().split())
operations = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]

basket = [n for n in range(1, N+1)]

for i, j in operations:
    basket[i-1:j] = reversed(basket[i-1:j])

print(*basket)