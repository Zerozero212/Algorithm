N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
idx = len(coins)-1
ans=0

while K:
    q = K // coins[idx]
    r = K % coins[idx]
    ans += q
    K = r
    idx -= 1

print(ans)