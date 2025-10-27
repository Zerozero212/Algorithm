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

N,M = map(int,input().split())

coor = [list(map(int,input().split())) for _ in range(N)]

graph=[]
for i in range(N-1):
    for j in range(i+1,N):
        w = ((coor[i][0]-coor[j][0])**2+(coor[i][1]-coor[j][1])**2)**0.5
        graph.append((i+1,j+1,w))
graph.sort(key=lambda x: x[2])

parents=[i for i in range(N+1)]

cnt=0
for _ in range(M):
    u,v = map(int,input().split())
    if union(u,v):
        cnt+=1

ans=0
for u,v,w in graph:
    if union(u,v):
        ans+=w
        cnt+=1
        if cnt==N-1:
            break

print(f'{round(ans,2):.2f}')