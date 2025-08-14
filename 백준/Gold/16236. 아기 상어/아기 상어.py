from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            sx, sy = i, j
            arr[i][j] = 0

baby_size = 2
baby_ate = 0
time = 0
dir1 = [(0,1),(0,-1),(1,0),(-1,0)]

while True:
    q = deque([(sx, sy, 0)])
    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True
    fish_list = []
    min_dist = float('inf')
    
    while q:
        x, y, d = q.popleft()
        if d > min_dist:
            break
        if 0 < arr[x][y] < baby_size:
            fish_list.append((x, y, d))
            min_dist = d
        for dx, dy in dir1:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and arr[nx][ny]<=baby_size:
                visited[nx][ny] = True
                q.append((nx, ny, d+1))
    
    if not fish_list:
        break
    
    fish_list.sort()
    fx, fy, dist = fish_list[0]
    
    sx, sy = fx, fy
    arr[fx][fy] = 0
    time += dist
    baby_ate += 1
    if baby_ate == baby_size:
        baby_ate = 0
        baby_size += 1

print(time)