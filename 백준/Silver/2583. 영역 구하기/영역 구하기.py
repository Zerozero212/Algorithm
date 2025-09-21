from collections import deque
dir1 = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(i,j):
    q = deque([(i,j)])
    area=0
    v[i][j]=1
    while q:
        x,y=q.popleft()
        area+=1
        for dx,dy in dir1:
            nx,ny=x+dx,y+dy
            if 0<=nx<M and 0<=ny<N and not v[nx][ny]:
                v[nx][ny]=1
                q.append((nx,ny))
    return area

M,N,K = map(int,input().split())
box = []
v=[[0]*N for _ in range(M)]

for _ in range(K):
    l_y,l_x,r_y,r_x = map(int,input().split())
    box.append((l_x,l_y,r_x,r_y))

for i_s,j_s,i_e,j_e in box:
    for i in range(i_s,i_e):
        for j in range(j_s,j_e):
            v[i][j]=1

answer=[]
for i in range(M):
    for j in range(N):
        if not v[i][j]: answer.append(bfs(i,j))

print(len(answer))
print(*sorted(answer))