def sol(k,path):
    if k==M: 
        print(*path)
        return
    for i in range(1,N+1):
        if v[i]: continue
        v[i]=1
        sol(k+1,path+[i])
        v[i]=0

N,M = map(int,input().split())
v=[0]*(N+1)
sol(0,[])