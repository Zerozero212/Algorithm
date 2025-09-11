N=int(input())
dp=[1,3]
if N<3: print(dp[N-1])
else:
    a,b=dp[0],dp[1]
    for _ in range(N-2):
        b,a=(2*a+b),b
    print(b%10007)