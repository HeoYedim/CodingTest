import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True
    count = 1

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    count += 1
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(dfs(i, j))

result.sort()

print(len(result))
for r in result:
    print(r)