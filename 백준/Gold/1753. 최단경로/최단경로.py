from heapq import heappush,heappop
INF=1e9
def daijkstra(start):
    dists=[INF]*(V+1)
    dists[start]=0
    heap=[(0,start)]

    while heap:
        dist,node = heappop(heap)
        if dists[node]<dist: continue

        for next_dist,next_node in nodes[node]:
            new_dist = dist + next_dist
            if new_dist<dists[next_node]:
                dists[next_node]=new_dist
                heappush(heap,(new_dist,next_node))
    return dists

V,E = map(int,input().split())
start = int(input())
nodes=[[] for _ in range(V+1)]
for _ in range(E):
    s,e,w = map(int,input().split())
    nodes[s].append((w,e))
ans=daijkstra(start)
for i in range(1,V+1):
    if ans[i]==INF:
        print('INF')
    else:
        print(ans[i])