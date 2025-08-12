dx = [1,1,-1,-1]
dy = [1,-1,-1,1]

def dfs(x,y,d,cnt):
    global n_max
    if 0 <= x < N and 0 <= y < N and d < 4:
        if d == 3 and (x,y) == (i,j): 
            n_max = max(n_max,cnt)
            return
        if v[arr[x][y]]: return 
        v[arr[x][y]] = 1
        nx, ny = x + dx[d], y + dy[d]
        dfs(nx,ny,d+1,cnt+1)
        dfs(nx,ny,d,cnt+1)
        v[arr[x][y]] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    v=[0]*101
    n_max = -1
    for i in range(N-2):
        for j in range(1,N-1):
            dfs(i,j,0,0)
    print(f'#{tc} {n_max}')