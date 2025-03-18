import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [False] * 100001

def bfs(n, k):
    queue = deque([(n, 0)])
    visited[n] = True

    while queue:
        x, time = queue.popleft()

        if x == k:
            return time

        for nx in [x - 1, x + 1, 2 * x]:
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time + 1))

    return -1

print(bfs(n, k))