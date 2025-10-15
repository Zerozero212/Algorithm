from heapq import heappush, heappop

def daijckstra(start,end=0):
    dists = [1e9]*(N+1)
    dists[start]=0
    heap = [(0,start)]

    while heap:
        d,n = heappop(heap)
        if n==end: return d
        if dists[n]<d: continue

        for nxt_d,nxt_n in graph[n]:
            new_d = d+nxt_d
            if new_d<dists[nxt_n]:
                dists[nxt_n]=new_d
                heappush(heap,(new_d,nxt_n))
    return dists

N,M,X = map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s].append((w,e))

ans=[]
back = daijckstra(X)
for i in range(1,N+1):
    if i==X: continue
    ans.append(daijckstra(i,X)+back[i])

print(max(ans))