dir1=[(0,1),(0,-1),(1,0),(-1,0)]
def dfs(x, y):
    global a
    for dx,dy in dir1:
        nx,ny=x+dx,y+dy
        if arr[nx][ny]==3: a=1
        elif not arr[nx][ny]:
            arr[nx][ny]=2
            dfs(nx,ny)
            arr[nx][ny]=0

for _ in range(10):
    a=0
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    dfs(1,1)
    print(f'#{tc} {a}')