from collections import deque

N=int(input())
q=deque([(0,N)])
while q:
    cnt,nq=q.popleft()
    if nq==1: break
    if nq%3==0: q.append((cnt+1,nq//3))
    if nq%2==0: q.append((cnt+1,nq//2))
    q.append((cnt+1,nq-1))

print(cnt)