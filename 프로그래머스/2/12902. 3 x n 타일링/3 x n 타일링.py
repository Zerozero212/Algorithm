def solution(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[2]=3
    for i in range(4,n+1,2):
        dp[i] = (4*dp[i-2] - dp[i-4])%(10**9+7)
    return dp[n]