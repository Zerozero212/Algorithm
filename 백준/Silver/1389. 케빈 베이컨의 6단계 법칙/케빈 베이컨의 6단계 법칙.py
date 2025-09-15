from collections import deque
def bfs(s):
    q=deque([(s,0)])
    v=[0]*(N+1)
    ans=[0]*(N+1)
    v[s]=1
    while q:
        start,depth=q.popleft()
        ans[start]=depth
        for num in graph[start]:
            if not v[num]: 
                v[num]=1
                q.append((num,depth+1))
    return ans

N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

ans=1e9
ans_num=0
for i in range(1,N+1):
    tmp=sum(bfs(i))
    if ans>tmp:
        ans=tmp
        ans_num=i
        
print(ans_num)