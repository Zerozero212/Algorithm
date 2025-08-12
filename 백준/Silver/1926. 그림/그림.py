from collections import deque
import sys
input = sys.stdin.readline

dir1 = [(-1,0),(1,0),(0,1),(0,-1)]

def bfs(x, y):
    global temp
    q = deque([(x,y)])
    v[x][y] = 1
    while q:
        i,j = q.popleft()
        temp += 1
        for di,dj in dir1:
            ni,nj = i+di,j+dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 1 and v[ni][nj] == 0:
                    v[ni][nj] = 1
                    q.append((ni,nj))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

count = 0
area_max = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and v[i][j] == 0:
            temp = 0
            bfs(i, j)
            count += 1
            # 함수 안에서 비교하게 되면, 다 탐색하기도 전에 비교하면서 오답이 나오기도 함.
            area_max = max(area_max, temp)

print(count)

print(area_max)
