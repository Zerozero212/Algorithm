dirs = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(selected, y_cnt):
    global cnt
    
    if y_cnt > 3: return
    
    if len(selected) == 7:
        fs = frozenset(selected)
        if fs not in seen: 
            seen.add(fs)
            cnt += 1
        return
    
    for x, y in selected:
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx,ny) not in selected:
                dfs(selected+[(nx,ny)], y_cnt + (arr[nx][ny]=='Y'))


arr = [list(input().strip()) for _ in range(5)]
cnt = 0
seen = set()

for i in range(5):
    for j in range(5):
        dfs([(i,j)], 1 if arr[i][j]=='Y' else 0)

print(cnt)
