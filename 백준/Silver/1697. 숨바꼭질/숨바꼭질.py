from collections import deque
def bfs(x,t):
    q = deque([(x,t)])
    v[x]=1
    while q:
        nx,nt = q.popleft()
        if nx == K: return nt
        if nx-1 >= 0 and v[nx-1] == 0:
            v[nx-1] = 1
            q.append((nx-1,nt+1))
        if nx+1 < 100001 and v[nx+1] == 0:
            v[nx+1] = 1
            q.append((nx+1,nt+1))
        if 2*nx < 100001 and v[2*nx] == 0:
            v[2*nx] = 1
            q.append((2*nx,nt+1))

N,K = map(int,input().split())
v = [0] * 100001
print(bfs(N,0))