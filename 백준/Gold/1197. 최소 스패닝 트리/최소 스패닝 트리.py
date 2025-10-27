from heapq import heappush, heappop
def prim():
    pq = [(0,1)]
    MST = [0]*(V+1)
    min_sum = 0

    while pq:
        w,node = heappop(pq)
        if MST[node]: continue
        MST[node]=1
        min_sum += w

        for nxt_w,nxt_node in graph[node]:
            if MST[nxt_node]: continue
            heappush(pq,(nxt_w,nxt_node))
    return min_sum

V,E = map(int,input().split())
graph=[[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))
    graph[v].append((w,u))

print(prim())