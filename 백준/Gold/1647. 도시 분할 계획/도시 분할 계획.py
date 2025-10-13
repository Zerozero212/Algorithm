def find_set(x):
    if x==parents[x]: return x
    parents[x]=find_set(parents[x])
    return parents[x]

def union(a,b):
    ra=find_set(a)
    rb=find_set(b)
    if ra==rb: return 0
    parents[ra]=rb
    return 1

N,M=map(int,input().split())
graph = []
for _ in range(M):
    u,v,w = map(int,input().split())
    graph.append((u,v,w))
graph.sort(key=lambda x:x[2])

parents = [i for i in range(N+1)]
ans=[]
cnt=0

for u,v,w in graph:
    if union(u,v):
        ans.append(w)
        cnt+=1
        if cnt==N-1: break

print(sum(ans)-max(ans))