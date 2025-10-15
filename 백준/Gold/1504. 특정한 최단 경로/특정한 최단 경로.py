from heapq import heappush,heappop
def sol(start,end):
    dists = [1e9]*(V+1)
    dists[start]=0
    pq = [(0,start)]

    while pq:
        dist,node = heappop(pq)
        if node == end: return dist
        if dists[node]<dist: continue
        for next_dist,next_node in graph[node]:
            new_dist = dist+next_dist
            if new_dist < dists[next_node]:
                dists[next_node]=new_dist
                heappush(pq,(new_dist,next_node))
    return -1

def valid():
    street1 = [sol(1,S1),sol(S1,S2),(sol(S2,V))]
    if -1 in street1: return -1
    street2 = [sol(1,S2),sol(S2,S1),(sol(S1,V))]
    if -1 in street2: return -1
    return min(sum(street1),sum(street2))

V,E = map(int,input().split())
graph=[[] for _ in range(V+1)]
for _ in range(E):
    n1,n2,w = map(int,input().split())
    graph[n1].append((w,n2))
    graph[n2].append((w,n1))
S1,S2 = map(int,input().split())

print(valid())