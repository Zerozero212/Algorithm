from collections import deque
def bfs(i,j):
    dir1=[(0,1),(0,-1),(1,0),(-1,0)]
    q=deque([(i,j,0)])
    wq=deque(water)
    while q:
        for _ in range(len(wq)):
            wx,wy=wq.popleft()
            for dwx,dwy in dir1:
                nwx,nwy=wx+dwx,wy+dwy
                if 0<=nwx<R and 0<=nwy<C and arr[nwx][nwy] in '.S':
                    arr[nwx][nwy]='*'
                    wq.append((nwx,nwy))
        
        for _ in range(len(q)):
            x,y,t=q.popleft()
            for dx,dy in dir1:
                nx,ny=x+dx,y+dy
                if 0<=nx<R and 0<=ny<C and arr[nx][ny] in '.D':
                    if (nx,ny)==target: return t+1
                    arr[nx][ny]='S'
                    q.append((nx,ny,t+1))
        
    return 'KAKTUS'


R,C = map(int,input().split())
arr = [list(input()) for _ in range(R)]

target = 0
me=0
water=[]

for i in range(R):
    for j in range(C):
        if arr[i][j]=='S': me=(i,j)
        elif arr[i][j]=='D': target=(i,j)
        elif arr[i][j]=='*': water.append((i,j))

print(bfs(*me))