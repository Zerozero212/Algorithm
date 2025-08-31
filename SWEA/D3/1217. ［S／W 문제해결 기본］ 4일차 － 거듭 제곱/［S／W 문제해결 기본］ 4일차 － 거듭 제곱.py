def sol(n,p):
    if p==1: return n
    return n*sol(n,p-1)

for t in range(1,11):
    N=input()
    n,p=map(int,input().split())
    print(f'#{t} {sol(n,p)}')