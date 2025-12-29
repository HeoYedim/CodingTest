import sys
input = sys.stdin.readline

N, D, K = map(int, input().split())
s = list(map(int, input().split()))

now = [0] * N
cnt = 0

for day in range(D):
    if any(now[i] + s[i] > K for i in range(N)):
        now = [0] * N
        cnt += 1

    for i in range(N):
        now[i] += s[i]

print(cnt)