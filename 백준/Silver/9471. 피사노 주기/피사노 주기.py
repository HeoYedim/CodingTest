import sys
input = sys.stdin.readline

def pisano_period(m) :
    prev, curr = 0, 1
    for i in range(1, m * m + 1):
        prev, curr = curr, (prev + curr) % m

        if prev == 0 and curr == 1:
            return i

P = int(input())
for _ in range(P):
    N, M = map(int, input().split())
    print(N, pisano_period(M))