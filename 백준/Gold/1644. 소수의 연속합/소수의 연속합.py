def get_li(n):
    tmp=[0,1]+[0]*(n-1)
    arr=[]
    for i in range(2,n//2+1):
        if tmp[i]: continue
        k=2
        while i*k<=n:
            tmp[i*k]=1
            k+=1
    return [idx for idx,val in enumerate(tmp) if idx>1 and not val]

N=int(input())
arr=get_li(N)
l=0
total=0
cnt=0

for r in arr:
    total+=r
    while total>N:
        total-=arr[l]
        l+=1
    if total==N: cnt+=1

print(cnt)