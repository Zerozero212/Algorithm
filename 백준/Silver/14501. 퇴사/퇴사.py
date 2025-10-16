N = int(input())
T = [0]
P = [0]
dp = [0] * (N + 2)  

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(N, 0, -1):
    tmp = i + T[i]
    if tmp <= N + 1:
        dp[i] = max(P[i] + dp[tmp], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])