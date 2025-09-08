N=int(input())
stair=[]
for _ in range(N):
    stair.append(int(input()))
if N==1: print(stair[0])
elif N==2: print(sum(stair))
else:
    dp=[0]*N
    dp[0],dp[1],dp[2]=stair[0],stair[0]+stair[1],max(stair[0],stair[1])+stair[2]

    for i in range(3,N):
        dp[i]=max(dp[i-3]+stair[i-1]+stair[i],dp[i-2]+stair[i])

    print(dp[N-1])