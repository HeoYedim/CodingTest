import sys
input = sys.stdin.readline

N, P = map(int, input().split())
melody = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
stack = [[] for _ in range(7)]

for now_string, now_fret in melody:
    while stack[now_string] and stack[now_string][-1] > now_fret:
            stack[now_string].pop()
            cnt += 1

    if not stack[now_string] or stack[now_string][-1] < now_fret:
        stack[now_string].append(now_fret)
        cnt += 1

print(cnt)