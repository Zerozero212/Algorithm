N,M=map(int,input().split())
arr=[0]+list(map(int,input().split()))
dp=arr[1:]
ans=0

for i in range(1,N):
    dp[i]+=dp[i-1]

for i in range(N):
    M+=arr[i]
    if M in set(dp[i:]): ans+=1

print(ans)