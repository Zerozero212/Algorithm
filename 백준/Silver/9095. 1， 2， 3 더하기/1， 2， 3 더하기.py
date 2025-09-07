from collections import deque
def sol():
    ans=0
    q=deque([(N,[])])
    while q:
        now,path=q.popleft()
        if not now: ans+=1 
        if now>0:
            if now-1>=0: q.append((now-1,path+[1]))
            if now-2>=0: q.append((now-2,path+[2]))
            if now-3>=0: q.append((now-3,path+[3]))
    return ans

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    print(sol())