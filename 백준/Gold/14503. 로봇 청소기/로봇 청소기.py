import sys
input = sys.stdin.readline

def clean_room(N, M, r, c, d, room):
    cleand_count = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    while True:
        if room[r][c] == 0:
            room[r][c] = 2
            cleand_count += 1
            
        found_cleanable = False
        for _ in range(4):
            d = (d + 3) % 4
            nr, nc = r + directions[d][0], c + directions[d][1]
            
            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
                r, c = nr, nc
                found_cleanable = True
                break
            
        if not found_cleanable:
            back_d = (d + 2) % 4
            br, bc = r + directions[back_d][0], c + directions[back_d][1]
                
            if 0 <= br < N and 0 <= bc < M and room[br][bc] != 1:
                r, c = br, bc
            else:
                break
            
    return cleand_count

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

print(clean_room(N, M, r, c, d, room))