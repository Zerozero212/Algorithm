from collections import deque
def sol():
    q=deque([(1,0)])
    v=[0]*(N+1)
    v[1]=-1

    while q:
        node,dist=q.popleft()

        for num in graph[node]:
            if not v[num]:
                v[num]=dist+1
                q.append((num,dist+1))
    M=max(v)
    return v.index(M),M,v.count(M)

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
print(*sol())