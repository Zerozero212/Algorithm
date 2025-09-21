from collections import deque
dir1=[(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)]

def bfs():
    q=deque()

    for z in range(H):
        for x in range(N):
            for y in range(M):
                if tomato[z][x][y]==1: q.append((x,y,z,0))

    while q:
        x,y,z,d=q.popleft()
        for dx,dy,dz in dir1:
            nx,ny,nz=x+dx,y+dy,z+dz
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and not tomato[nz][nx][ny]:
                tomato[nz][nx][ny]=1
                q.append((nx,ny,nz,d+1))

    for z in range(H):
        for x in range(N):
            for y in range(M):
                if not tomato[z][x][y]: return -1
    
    return d

M,N,H = map(int,input().split())
tomato = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
print(bfs())