def sol(n):
    dp=[0]*(n+3)
    dp[1],dp[2],dp[3]=1,2,3
    if n<4: return dp[n]

    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]%10007

N=int(input())
print(sol(N))