from collections import deque
def bfs(n):
    q=deque([(n,0)])
    cnt=0
    while q:
        num,depth=q.popleft()
        if 0<depth<3: cnt+=1
        if depth>2: break
        for nn in graph[num]:
            if v[nn]: continue
            v[nn]=1
            q.append((nn,depth+1))
    return cnt

N=int(input())
E=int(input())
graph=[[] for _ in range(N+1)]
v=[0]*(N+1)
v[1]=1
for _ in range(E):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

print(bfs(1))