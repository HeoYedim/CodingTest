import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
canvas = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j):
    size = 1
    visited[i][j] = True

    for d in range(4):
        nx, ny = i + dx[d], j + dy[d]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and canvas[nx][ny]:
            size += dfs(nx, ny)

    return size

count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1 and not visited[i][j]:
            count += 1
            max_size = max(max_size, dfs(i, j))

print(count)
print(max_size)