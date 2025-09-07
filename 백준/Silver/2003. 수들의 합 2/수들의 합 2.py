N,M=map(int,input().split())
arr=[0]+list(map(int,input().split()))
dp=arr[1:]
ans=0

for i in range(1,N):
    dp[i]+=dp[i-1]

# 1. 1 1 1 1이 주어졌다고 가정하자. 누적합으로 1 2 3 4를 구하고 시작
# 2. M이 있는지 확인 > 이는 곧, i가 0이고 j는 1부터 N-1까지인 경우
# 3. 핵심 KEY POINT : 이제 i가 1인 경우를 구하고 싶은데, idx==0인 값을 나머지에 빼기에는 N-1번 돌아야 하기에 비효율적
# 따라서, 1 2 3 4 를 그대로 활용하되, M에 idx==0인 경우를 더하여 탐색
# 2 3 4에서 M = M+arr[0]한 3이 있는지 탐색
# 이와 같은 방법으로 끝까지 탐색
for i in range(N):
    M+=arr[i]
    if M in set(dp[i:]): ans+=1


print(ans)
