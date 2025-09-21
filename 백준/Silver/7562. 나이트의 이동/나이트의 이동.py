from collections import deque
dir1 = [(-1,-2),(-2,-1),(-1,2),(-2,1),(1,-2),(1,2),(2,-1),(2,1)]
def bfs(i,j):
    q=deque([(i,j,0)])
    v[i][j]=1
    while q:
        x,y,c=q.popleft()
        if (x,y)==(t_x,t_y): return c
        for dx,dy in dir1:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and not v[nx][ny]:
                v[nx][ny]=1
                q.append((nx,ny,c+1))

T=int(input())
for tc in range(T):
    N=int(input())
    v=[[0]*N for _ in range(N)]
    c_x,c_y = map(int,input().split())
    t_x,t_y = map(int,input().split())
    
    if (c_x,c_y) == (t_x,t_y): print(0)
    else:print(bfs(c_x,c_y))