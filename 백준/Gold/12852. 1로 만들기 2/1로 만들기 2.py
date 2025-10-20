from heapq import heappush,heappop
def sol():
    pq = [(0,1)]
    cnt=[1e9]*(N+1)
    cnt[1]=0
    v=[0]*(N+1)

    while pq:
        k,num = heappop(pq)
        if v[num]: continue
        if num==N: return k
        v[num]=1

        for nxt in (num+1,num*2,num*3):
            if nxt<=N and k+1<cnt[nxt]:
                cnt[nxt]=k+1
                prev[nxt]=num
                heappush(pq,(k+1,nxt))

N=int(input())
prev=[0]*(N+1)
ans=sol()
print(ans)

while N:
    print(N,end=' ')
    N=prev[N]