from collections import deque

dir1 = [(0,1),(0,-1),(1,0),(-1,0)]

# 상어로부터 물고기까지의 최소 거리 구하는 함수
def find_min_path(fx, fy, nx, ny, size):
    v = [[0]*N for _ in range(N)]
    q = deque([(nx, ny, 0)])
    v[nx][ny] = 1
    while q:
        i, j, nd = q.popleft()
        if (i, j) == (fx, fy):
            return nd
        for di, dj in dir1:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and arr[ni][nj] <= size:
                v[ni][nj] = 1
                q.append((ni, nj, nd + 1))
    return None  # 도달 불가 시 None 반환

# 물고기까지의 최소 거리를 찾고, 물고기의 좌표와 걸리는 시간을 반환
def check_fish_xy(arr1, size, nx, ny):
    d_min = float('inf')
    min_x, min_y = -1, -1
    until = min(size, 7)
    
    for i in range(1, until):
        for x, y in arr1[i]:
            temp_min = find_min_path(x, y, nx, ny, size)
            if temp_min is None:
                continue
            if temp_min < d_min:
                d_min = temp_min
                min_x, min_y = x, y
            elif temp_min == d_min:
                # 거리 같으면 가장 위(x 작은) → 그 다음 가장 왼쪽(y 작은)
                if x < min_x or (x == min_x and y < min_y):
                    min_x, min_y = x, y
    if min_x == -1:  # 먹을 수 있는 물고기 없음
        return (-1, -1, 0)
    return (min_x, min_y, d_min)

# 상어가 먹을 수 있는 물고기 있는지 확인
def valid(arr, size):
    until = min(size, 7)
    for i in range(1, until):
        if arr[i]:
            return True
    return False

# 입력 처리
N = int(input())
baby_size = 2
baby_ate_fish = 0
time = 0

fish_arr = {i: [] for i in range(1, 7)}
fish_arr[9] = []
arr = []

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j]:
            fish_arr[temp[j]].append([i, j])
    arr.append(temp)

# 아기 상어 시뮬레이션
while valid(fish_arr, baby_size):
    move_x, move_y, dt = check_fish_xy(fish_arr, baby_size, fish_arr[9][0][0], fish_arr[9][0][1])
    if move_x == -1:  # 더 이상 먹을 수 있는 물고기 없음
        break
    
    # 물고기 제거
    fish_arr[arr[move_x][move_y]].remove([move_x, move_y])
    baby_ate_fish += 1
    if baby_ate_fish == baby_size:
        baby_ate_fish = 0
        baby_size += 1
    
    # 상어 위치 업데이트
    arr[fish_arr[9][0][0]][fish_arr[9][0][1]] = 0
    fish_arr[9][0][0] = move_x
    fish_arr[9][0][1] = move_y
    arr[move_x][move_y] = 9
    
    # 시간 누적
    time += dt

print(time)
