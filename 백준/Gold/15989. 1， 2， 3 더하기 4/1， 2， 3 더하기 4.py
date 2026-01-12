N = int(input())
arr = [int(input()) for _ in range(N)]
target = max(arr) + 1

dp = [0] * 10001
dp[0] = 1

for i in range(1,target):
    dp[i] += dp[i-1]

for i in range(2,target):
    dp[i] += dp[i-2]

for i in range(3,target):
    dp[i] += dp[i-3]

for n in arr:
    print(dp[n])