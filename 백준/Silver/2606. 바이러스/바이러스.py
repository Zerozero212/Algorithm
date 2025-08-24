from collections import deque

N=int(input())
E=int(input())
node=[[] for _ in range(N+1)]
v=[0]*(N+1)
for _ in range(E):
    n1,n2=map(int,input().split())
    node[n1].append(n2)
    node[n2].append(n1)

q=deque([1])
v[1]=1
while q:
    nn=q.popleft()
    for num in node[nn]:
        if not v[num]: 
            v[num]=1
            q.append(num)
            v[0]+=1
print(v[0])