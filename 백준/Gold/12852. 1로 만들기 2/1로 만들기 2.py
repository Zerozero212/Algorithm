## heap 자료구조를 활용한 풀이
# from heapq import heappush,heappop
# def sol():
#     pq = [(0,1)]
#     cnt=[1e9]*(N+1)
#     cnt[1]=0
#     v=[0]*(N+1)

#     while pq:
#         k,num = heappop(pq)
#         if v[num]: continue
#         if num==N: return k
#         v[num]=1

#         for nxt in (num+1,num*2,num*3):
#             if nxt<=N and k+1<cnt[nxt]:
#                 cnt[nxt]=k+1
#                 prev[nxt]=num
#                 heappush(pq,(k+1,nxt))

# N=int(input())
# prev=[0]*(N+1)
# ans=sol()
# print(ans)

# while N:
#     print(N,end=' ')
#     N=prev[N]

N = int(input())
dp = [0]*(N+1)
prev = [0]*(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    prev[i] = i-1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        prev[i] = i//2
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        prev[i] = i//3

print(dp[N])

while N:
    print(N,end=' ')

    N = prev[N]
