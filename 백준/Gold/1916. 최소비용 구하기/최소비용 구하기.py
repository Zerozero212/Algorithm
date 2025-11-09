from heapq import heappush,heappop
INF = 10**12
def sol(s):
    dists = [INF]*(N+1)
    dists[s]=0
    pq = [(0,s)]

    while pq:
        d,n = heappop(pq)
        if n==e: return d
        if dists[n]<d: continue

        for nxt_d,nxt_n in graph[n]:
            new_d = d+nxt_d
            if new_d < dists[nxt_n]:
                dists[nxt_n]=new_d
                heappush(pq,(new_d,nxt_n))


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
s,e = map(int,input().split())
print(sol(s))