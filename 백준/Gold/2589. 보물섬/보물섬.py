from collections import deque
dir1 = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(i,j):
    global ans
    q = deque([(0,i,j)])
    v=[[0]*M for _ in range(N)]
    v[i][j]=1

    while q:
        cnt,x,y = q.popleft()
        ans = max(ans,cnt)
        for dx,dy in dir1:
            nx,ny = x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and v[nx][ny]==0 and arr[nx][ny]=='L':
                v[nx][ny]=1
                q.append((cnt+1,nx,ny))

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
ans=0

for i in range(N):
    for j in range(M):
        if arr[i][j]=='L': bfs(i,j)

print(ans)