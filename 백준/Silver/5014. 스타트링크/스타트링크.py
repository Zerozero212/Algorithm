from collections import deque
def bfs(s):
    v=[0]*(F+1)
    q=deque([(s,0)])
    v[s]=1
    while q:
        floor,cnt = q.popleft()
        if floor == G: return cnt
        for move in [U,-D]:
            next = floor+move
            if 1<=next<=F and not v[next]:
                v[next]=1
                q.append((next,cnt+1))
    return 'use the stairs'

F,S,G,U,D = map(int,input().split())
print(bfs(S))