T=int(input())
for tc in range(T):
    N=int(input())
    dp=[0]*(10**6+1)
    dp[0]=dp[1]=1
    dp[2]=2

    for i in range(3,N+1):
        dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%(10**9+9)
    
    print(dp[N])