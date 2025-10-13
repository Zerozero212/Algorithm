from collections import deque
N=int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    n1,n2 = map(int,input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

parent=[0]*(N+1)
v=[0]*(N+1)
q=deque([1])
cnt=0

while q:
    node = q.popleft()

    if v[node]: continue
    v[node]=1

    for next in tree[node]:
        if not v[next]:
            parent[next]=node
            q.append(next)

for i in range(2,N+1):
    print(parent[i])