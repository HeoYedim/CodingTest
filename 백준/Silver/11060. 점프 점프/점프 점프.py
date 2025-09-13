import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
grid = list(map(int, input().split()))
visited = [-1] * N
visited[0] = 0
q = deque([0])

while q:
    x = q.popleft()
    for nx in range(x + 1, x + grid[x] + 1):
        if nx >= N:
            break
        if visited[nx] == -1:
            visited[nx] = visited[x] + 1
            q.append(nx)

print(visited[-1])