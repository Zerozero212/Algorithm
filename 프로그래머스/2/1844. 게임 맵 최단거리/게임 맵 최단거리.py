from collections import deque
def solution(maps):
    N,M=len(maps),len(maps[0])
    dir1=[(0,1),(0,-1),(1,0),(-1,0)]
    v=[[0]*M for _ in range(N)]
    q=deque([(0,0)])
    v[0][0]=1
    while q:
        x,y=q.popleft()
        if x==N-1 and y==M-1: return maps[x][y]
        for dx,dy in dir1:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<M and maps[nx][ny] and not v[nx][ny]:
                v[nx][ny]=1
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
    return -1