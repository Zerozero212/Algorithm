import sys

def sol(n,total):
    if n<0: return
    
    if n==0:
        for i in range(1,total,2):
            ans[i]=' '
        return
    
    for i in range(3**n,total,2*3**n):
        ans[i:i+3**n]=' '*3**n
    sol(n-1,total)

for line in sys.stdin:
    N=int(line.strip())
    ans=['-']*3**N
    sol(N-1,len(ans))
    print(''.join(ans))