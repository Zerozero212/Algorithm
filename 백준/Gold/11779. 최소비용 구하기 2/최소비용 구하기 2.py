from heapq import heappush, heappop
def daijckstra(start,end):
    dists=[1e9]*(city+1)
    dists[start]=0
    heap = [[0,start,[start]]]

    while heap:
        d,n,path = heappop(heap)
        if n==end: return d,path
        if dists[n]<d: continue

        for nxt_d,nxt_n in bus[n]:
            new_d = d+nxt_d
            if new_d<dists[nxt_n]:
                dists[nxt_n]=new_d
                heappush(heap,(new_d,nxt_n,path+[nxt_n]))

city=int(input())
M=int(input())
bus=[[] for _ in range(city+1)]
for _ in range(M):
    s,e,w = map(int,input().split())
    bus[s].append((w,e))
start,end = map(int,input().split())

dist,path = daijckstra(start,end)
print(dist)
print(len(path))
print(*path)