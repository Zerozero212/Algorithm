N = int(input())
arr = list(map(int,input().split()))

l,r = 0,N-1
ans = 10**18
ans_i,ans_j = 0,0

while l<r:
    s = arr[l]+arr[r]
    if abs(s)<ans:
        ans=abs(s)
        ans_i,ans_j=l,r
        if not ans: break
    
    if s>0: r-=1
    else: l+=1

print(arr[ans_i],arr[ans_j])