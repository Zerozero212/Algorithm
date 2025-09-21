from collections import deque
dir1 = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(x,y):
    q = deque([(x,y)])
    soil[x][y]=2
    while q:
        i,j = q.popleft()
        for di,dj in dir1:
            ni,nj=i+di,j+dj
            if 0<=ni<R and 0<=nj<C and soil[ni][nj]==1:
                soil[ni][nj]=2
                q.append((ni,nj))

T=int(input())
for tc in range(1,T+1):
    R,C,cnt = map(int,input().split())
    soil = [[0]*C for _ in range(R)]
    ans=0

    for _ in range(cnt):
        x,y = map(int,input().split())
        soil[x][y]=1

    for x in range(R):
        for y in range(C):
            if soil[x][y]==1:
                bfs(x,y)
                ans+=1

    print(ans)