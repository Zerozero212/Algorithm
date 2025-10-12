from heapq import heappush,heappop
def prim(start_node):
    pq=[(0,start_node)]
    MST = [0]*N
    min_weight=0

    while pq:
        weight,node = heappop(pq)
        if MST[node]: continue
        MST[node]=1
        min_weight+=weight

        for next_node in range(N):
            if node == next_node: continue
            if MST[next_node]: continue
            heappush(pq,(graph[node][next_node],next_node))
    return min_weight

N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
result = prim(0)
print(result)