import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

L = a[0] - K + 1
R = a[0]
cnt = 0

for gunban in a[1:]:
    nextLeft = gunban - K + 1
    nextRight = gunban

    newLeft = max(L, nextLeft)
    newRight = min(R, nextRight)

    if newLeft > newRight:
        cnt += 1
        L = nextLeft
        R = nextRight
    else:
        L = newLeft
        R = newRight

print(cnt)