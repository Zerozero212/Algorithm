dir1 = [(-1,0),(1,0),(0,-1),(0,1)]

def dfs(x, y, length_now, cut_used):
    global best_length
    visited[x][y] = 1
    moved = False

    for dx, dy in dir1:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            # 그냥 이동 가능
            if arr[nx][ny] < arr[x][y]:
                moved = True
                dfs(nx, ny, length_now + 1, cut_used)
            # 공사해서 이동 가능
            elif not cut_used and arr[nx][ny] - K < arr[x][y]:
                original_height = arr[nx][ny]
                for k in range(1, K+1):
                    arr[nx][ny] = original_height - k
                    if arr[nx][ny] < arr[x][y]:
                        moved = True
                        dfs(nx, ny, length_now + 1, 1)
                arr[nx][ny] = original_height

    visited[x][y] = 0  # 백트래킹
    if not moved:
        best_length = max(best_length, length_now)

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 최대 높이 봉우리 찾기
    max_height = max(max(row) for row in arr)
    peaks = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == max_height]

    best_length = 0
    for sx, sy in peaks:
        visited = [[0]*N for _ in range(N)]
        dfs(sx, sy, 1, 0)

    print(f'#{tc} {best_length}')
