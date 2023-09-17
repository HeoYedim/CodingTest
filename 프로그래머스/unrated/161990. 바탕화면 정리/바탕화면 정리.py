def solution(wallpaper):
    col,row = [],[]
    
    for c in range(len(wallpaper)):
        for r in range(len(wallpaper[0])):
            if wallpaper[c][r] == "#":
                col.append(c)
                row.append(r)
    
    return [min(col), min(row), max(col)+1, max(row)+1]