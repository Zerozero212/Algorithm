def find_set(x):
    if x==parents[x]: return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(a,b):
    ra = find_set(a)
    rb = find_set(b)
    if ra==rb: return 0
    parents[ra]=rb
    return 1

V,E = map(int,input().split())
graph = []
for _ in range(E):
    u,v,w = map(int,input().split())
    graph.append((u,v,w))

graph.sort(key=lambda x: x[2])
parents=[i for i in range(V+1)]
cnt=0
ans=0

for u,v,w in graph:
    if union(u,v):
        cnt+=1
        ans+=w
        if cnt==V-1: break

print(ans)