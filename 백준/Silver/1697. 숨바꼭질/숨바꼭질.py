from collections import deque

def bfs():
    q = deque([N])
    v[N] = 1
    while q:
        x = q.popleft()
        if x == K:
            return v[x] - 1  # 시작을 1로 뒀으니 최종 시간은 -1
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and v[nx] == 0:
                v[nx] = v[x] + 1
                q.append(nx)

N, K = map(int, input().split())
v = [0] * 100001
print(bfs())
