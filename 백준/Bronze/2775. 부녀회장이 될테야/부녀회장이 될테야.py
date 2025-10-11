N=int(input())
for _ in range(N):
    k=int(input())
    n=int(input())
    dp=[[i for i in range(n+1)]] + [[0]*(n+1) for _ in range(k)]

    for floor in range(1,k+1):
        for room in range(1,n+1):
            if room==1: dp[floor][room]=dp[floor-1][room]
            else: dp[floor][room]=dp[floor][room-1]+dp[floor-1][room]
    
    print(dp[k][n])