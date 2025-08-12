from collections import deque
dir1 = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x,y,version):
    if v[x][y]: return 0
    q = deque([(x,y)])
    v[x][y] = 1
    ch = arr[version][x][y]
    while q:
        i,j = q.popleft()
        for di,dj in dir1:
            ni,nj = i+di,j+dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[version][ni][nj] == ch:
                v[ni][nj] = 1
                q.append((ni,nj))
    return 1

N = int(input())
arr1 = [input() for _ in range(N)]
arr2 = [row.replace('R','G') for row in arr1]
arr = [arr1,arr2]
count = [0,0]
for tc in range(2):
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if bfs(i,j,tc): count[tc] += 1
print(count[0],count[1])