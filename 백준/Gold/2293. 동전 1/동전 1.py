N,K = map(int,input().split())
coin_list = sorted([int(input()) for _ in range(N)],reverse=True)

dp=[0]*(K+1)
dp[0]=1

for coin in coin_list:
    for idx in range(K+1):
        if idx-coin>=0:
            dp[idx] += dp[idx-coin]

print(dp[K])