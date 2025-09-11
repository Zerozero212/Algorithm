def sol(n):
    for i in range(2,n):
        dp[i][0]=dp[i-1][1]+dp[i-1][0]
        dp[i][1]=dp[i-1][0]

N=int(input())
dp=[[0]*2 for _ in range(90)]
dp[0][1]=1
dp[1][0]=1

if N<3: print(1)
else:
    sol(N)
    print(sum(dp[N-1]))