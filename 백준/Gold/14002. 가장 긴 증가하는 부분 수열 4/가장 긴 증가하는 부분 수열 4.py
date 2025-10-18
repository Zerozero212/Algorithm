N = int(input())
arr = list(map(int,input().split()))
dp=[0]*1001
path = [[] for _ in range(1001)]

for num in arr:
    idx = dp[:num].index(max(dp[:num]))
    dp[num] = dp[idx] + 1
    path[num] = path[idx] + [num]

idx = dp.index(max(dp))
print(dp[idx])
print(*path[idx])