def dfs(n):
    v[n]=1
    for num in graph[n]:
        if v[num]: continue
        dfs(num)

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

v=[0]*(N+1)
ans=0
for i in range(1,N+1):
    if v[i]: continue
    dfs(i)
    ans+=1

print(ans)