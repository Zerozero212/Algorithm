N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dp[x][y][d]: (x,y)에 끝이 있고 방향이 d인 경우의 수
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

# 초기값: (0,1)에 가로로 놓여 있음
dp[0][1][0] = 1

for x in range(N):
    for y in range(N):
        if arr[x][y] == 1:  # 벽이면 불가
            continue
        # 가로
        if y-1 >= 0 and arr[x][y-1] == 0:
            dp[x][y][0] += dp[x][y-1][0] + dp[x][y-1][2]
        # 세로
        if x-1 >= 0 and arr[x-1][y] == 0:
            dp[x][y][1] += dp[x-1][y][1] + dp[x-1][y][2]
        # 대각선
        if x-1 >= 0 and y-1 >= 0:
            if arr[x-1][y] == 0 and arr[x][y-1] == 0 and arr[x-1][y-1] == 0:
                dp[x][y][2] += sum(dp[x-1][y-1])

print(sum(dp[N-1][N-1]))
