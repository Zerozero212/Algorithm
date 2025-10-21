N=int(input())
consulting = [tuple(map(int,input().split())) for _ in range(N)]
dp=[0]*(N+1)

for i in range(N-1,-1,-1):
    end_date = i+consulting[i][0]
    if end_date<=N:
        dp[i] = max(dp[end_date] + consulting[i][1],dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])