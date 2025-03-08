import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

print('Yes' if sum(a * b for a, b in items) == X else 'No')