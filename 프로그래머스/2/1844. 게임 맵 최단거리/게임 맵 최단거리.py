from collections import deque

def solution(maps):
    # maps size (m*n)
    m = len(maps)
    n = len(maps[0])
    
    visited = [[False] * n for _ in range(m)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(0, 0)])
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        if x == (m - 1) and y == (n - 1):
            return maps[x][y]
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
    
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                
    return -1