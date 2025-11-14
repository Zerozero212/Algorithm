from collections import deque

N,K = map(int,input().split())
q = deque([N])
position = [0]*(10**5+1)
visited = [0]*(10**5+1)
visited[N]=1

while q:
    x = q.popleft()

    if x==K: 
        print(position[x])
        break

    if 0<=2*x<=10**5 and visited[2*x]==0:
        position[2*x] = position[x]
        visited[2*x]=1
        q.append(2*x)

    for nx in (x-1,x+1):
        if 0<=nx<=10**5 and visited[nx]==0:
            position[nx] = position[x]+1
            visited[nx]=1
            q.append(nx)