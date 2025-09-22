import sys
input = sys.stdin.readline
from collections import deque
dir1=[(0,1),(0,-1),(1,0),(-1,0)]

def bfs(i,j):
    v[i][j]=1
    q=deque([(i,j)])
    while q:
        x,y=q.popleft()
        for dx,dy in dir1:
            nx,ny=x+dx,y+dy
            if 0<=nx<N and 0<=ny<N and arr[nx][ny] and not v[nx][ny]:
                v[nx][ny]=1
                q.append((nx,ny))

N=int(input())
max_n=0
arr=[]
for _ in range(N):
    tmp=list(map(int,input().split()))
    arr.append(tmp)
    max_n=max(max_n,max(tmp))

ans=1
for num in range(1,max_n):
    v=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]==num:
                arr[i][j]=0
    
    tmp=0
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not v[i][j]:
                bfs(i,j)
                tmp+=1
    ans=max(ans,tmp)

print(ans)