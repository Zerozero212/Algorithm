from collections import deque
dir1=[(0,1),(0,-1),(1,0),(-1,0)]
def bfs(i,j):
    q=deque([(i,j)])
    arr[i][j]=0
    cnt=0

    while q:
        x,y=q.popleft()
        cnt+=1
        for dx,dy in dir1:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]:
                arr[nx][ny]=0
                q.append((nx,ny))
    
    return cnt

N=int(input())
arr=[list(map(int,input())) for _ in range(N)]

ans=[]
for i in range(N):
    for j in range(N):
        if arr[i][j]: ans.append(bfs(i,j))

ans.sort()
print(len(ans))
for n in ans:
    print(n)