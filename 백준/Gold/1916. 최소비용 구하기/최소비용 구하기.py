from heapq import heappop,heappush
INF=1e9
city=int(input())
bus=int(input())

bus_cost = [[] for _ in range(city+1)]

for _ in range(bus):
    s,e,c = map(int,input().split())
    bus_cost[s].append((c,e))
start,end=map(int,input().split())

pq = [(0,start)]
dists=[INF]*(city+1)
dists[start]=0

while pq:
    dist,node = heappop(pq)
    if dists[node] < dist: continue

    for next_dist,next_node in bus_cost[node]:
        new_cost = dist+next_dist
        if new_cost < dists[next_node]:
            dists[next_node]=new_cost
            heappush(pq,(new_cost,next_node))

print(dists[end])