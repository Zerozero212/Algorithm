def sol(n,r,c):
    if not n: return 0
    std = 2**(n-1)
    
    if r<std and c<std: return sol(n-1,r,c)
    elif r<std and c>=std: return std**2 + sol(n-1,r,c-std)
    elif r>=std and c<std: return 2*std**2 + sol(n-1,r-std,c)
    elif r>=std and c>=std: return 3*std**2 + sol(n-1,r-std,c-std)

N,r,c = map(int,input().split())
print(sol(N,r,c))