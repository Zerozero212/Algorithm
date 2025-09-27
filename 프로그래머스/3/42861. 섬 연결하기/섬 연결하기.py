from heapq import heappop,heappush
def solution(n, costs):
    ans=0
    graph=[[] for _ in range(n)]
    for s,e,w in costs:
        graph[s].append((w,e))
        graph[e].append((w,s))
    
    MST=[0]*n
    pq=[(0,0)]
    
    while pq:
        w,n = heappop(pq)
        if MST[n]: continue
        MST[n]=1
        ans+=w
        for nw,nn in graph[n]:
            if not MST[nn]:
                heappush(pq,(nw,nn))
    
    return ans