import sys

n, m = map(int, sys.stdin.readline().split())
battlefield = [list(sys.stdin.readline().strip()) for _ in range(m)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * n for _ in range(m)]

def dfs(x, y, team):
    stack = [(x, y)]
    visited[y][x] = True
    count = 1

    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[ny][nx] and battlefield[ny][nx] == team:
                    visited[ny][nx] = True
                    stack.append((nx, ny))
                    count += 1

    return count

white_power = 0
blue_power = 0

for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            team = battlefield[y][x]
            soldiers = dfs(x, y, team)
            if team == 'W':
                white_power += soldiers ** 2
            else:
                blue_power += soldiers ** 2

print(white_power, blue_power)