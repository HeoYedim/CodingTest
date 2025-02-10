n = int(input())
m = int(input())
network = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

def dfs(start):
    stack = [start]
    visited = [False] * (n + 1)
    visited[start] = True
    count = 0

    while stack:
        node = stack.pop()
        for neighbor in network[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                count += 1

    return count

print(dfs(1))