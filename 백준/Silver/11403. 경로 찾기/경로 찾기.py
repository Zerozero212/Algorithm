def dfs(s,e):
    global tool
    v[s]=1
    
    for i in graph[s]:
        if i==e: 
            tool=1
            return
        if v[i]: continue
        v[i]=1
        dfs(i,e)


N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
graph=[[] for _ in range(N)]
ans=[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j]: graph[i].append(j)

for i in range(N):
    for j in range(N):
        v=[0]*N
        tool=0
        dfs(i,j)
        ans[i][j]=tool

for row in ans:
    print(*row)