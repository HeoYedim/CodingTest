import sys
sys.setrecursionlimit(1000000)

N = int(input())
drawing = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

# 동사남북 델타 변수 d
d = [(0,1), (0, -1), (1,0), (-1,0)]

def dfs(x, y):
    # 현재 칸 방문 처리
    visited[y][x] = True
    # 이동할 칸과의 색 비교를 위한 현재 칸 색상 변수
    color = drawing[y][x]
    # 동서남북 같은 색상 유무 확인
    for dx, dy in d:
        # X, Y는 동서남북 이동할 칸의 좌표
        X, Y = x + dx, y + dy
        # N * N 칸에서 이동할 수 있도록 제한
        if (0 <= X < N) and (0 <= Y < N):
            if visited[Y][X] == False and drawing[Y][X] == color:
                dfs(X, Y)

RGB, RRB = 0, 0

# 적록색맹이 아닌 경우
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            dfs(x,y)
            RGB += 1

# G -> R 수정
for y in range(N):
    for x in range(N):
        if drawing[y][x] == 'G':
            drawing[y][x] = 'R'
visited = [[False] * N for _ in range(N)]

# 적록색맹인 경우
for y in range(N):
    for x in range(N):
        if visited[y][x] == False:
            dfs(x, y)
            RRB += 1

print(RGB, RRB)