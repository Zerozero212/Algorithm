N=int(input())
ans=[0,1]
if N<2: print(ans[N])
else:
    a,b=ans[0],ans[1]
    for _ in range(1,N):
        b,a=a+b,b
    print(b)