N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]

dp=[[0]*3 for _ in range(N)]
dp[0]=house[0]

for i in range(1,N):
    for j in range(3):
        dp[i][j] = house[i][j] + min(dp[i-1][:j]+dp[i-1][j+1:])

print(min(dp[N-1]))