from collections import deque
dir1 = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y,count):
    q=deque([(x,y,count)])
    v[x][y] = 1
    while q:
        i,j,count_now = q.popleft()
        if (i,j) == (N-1,M-1): return count_now
        for di,dj in dir1:
            ni,nj = i+di,j+dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] and v[ni][nj] == 0:
                    q.append((ni,nj,count_now+1))
                    v[ni][nj] = 1

N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]
v = [[0]*M for _ in range(N)]
print(bfs(0,0,1))