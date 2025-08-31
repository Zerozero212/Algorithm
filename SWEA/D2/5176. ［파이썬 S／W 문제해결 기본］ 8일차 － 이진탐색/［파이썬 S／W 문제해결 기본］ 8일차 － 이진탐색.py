def sol(n):
    global node
    if n>N: return
    sol(2*n)
    v[n]=node
    node+=1
    sol(2*n+1)

T=int(input())
for t in range(1,T+1):
    N=int(input())
    v=[0]*(N+1)
    node=1
    sol(1)
    print(f'#{t} {v[1]} {v[N//2]}')