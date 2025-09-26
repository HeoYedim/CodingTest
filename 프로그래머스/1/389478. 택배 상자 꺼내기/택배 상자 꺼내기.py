def solution(n, w, num):
    boxs =[[0] * w for _ in range((n + w - 1) // w)]
    cnt = 1
    
    for i in range(0, len(boxs)):
        for j in range(0, w):
            if cnt > n:
                break
            boxs[i][j] = cnt
            cnt += 1
            
        if i % 2 != 0:
            boxs[i].reverse()
            
    row, col = -1, -1
    for r in range(len(boxs)):
        for c in range(w):
            if boxs[r][c] == num:
                row, col = r, c
                break 
            
    box_count = 0
    for r in range(row, len(boxs)):
        if boxs[r][col] != 0:
            box_count += 1
            
    return box_count