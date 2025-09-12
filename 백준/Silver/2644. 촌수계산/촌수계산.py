import sys
input = sys.stdin.readline

n = int(input())
A, B = map(int, input().split())
m = int(input())
family = [[] for _ in range(n + 1)]
for _ in range(m):
    parent, children = map(int, input().split())
    family[parent].append(children)
    family[children].append(parent)

visited = [-1] * (n + 1)

def dfs(current):
    for child in family[current]:
        if visited[child] == -1:
            visited[child] = visited[current] + 1
            dfs(child)
visited[B] = 0
dfs(B)

print(visited[A])