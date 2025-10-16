def sol(cnt,idx,path):
    if cnt==M:
        print(*path)
        return
    
    for i in range(idx,N+1):
        if v[i]: continue
        v[i]=1
        sol(cnt+1,i+1,path+[i])
        v[i]=0

N,M = map(int,input().split())

v=[0]*(N+1)
sol(0,1,[])