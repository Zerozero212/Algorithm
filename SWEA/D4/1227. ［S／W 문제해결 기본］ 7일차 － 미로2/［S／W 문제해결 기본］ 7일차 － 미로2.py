dir1=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(i,j):
    q=[(i,j)]
    while q:
        x,y=q.pop(0)
        for dx,dy in dir1:
            nx,ny=x+dx,y+dy
            if arr[nx][ny] in set((0,3)):
                if arr[nx][ny]==3: return 1
                arr[nx][ny]=2
                q.append((nx,ny))
    return 0

for t in range(1,11):
    a=input()
    arr=[list(map(int,input())) for _ in range(100)]
    print(f'#{t} {bfs(1,1)}')