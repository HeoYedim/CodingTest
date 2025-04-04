import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0

for i in range(N):
    answer += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(answer)