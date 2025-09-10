import sys
input = sys.stdin.readline

N,S=map(int,input().split())
arr=list(map(int,input().split()))

i=j=0
sub_sum=arr[i]
min_len=float('inf') 
while i<=j<N:
    while j<N-1 and sub_sum<S:
        j+=1
        sub_sum+=arr[j]
    if sub_sum>=S:
        min_len=min(min_len,j-i+1)
        if i==j and j<N:
            j+=1
            if j==N: break
            sub_sum+=arr[j]
        if i<N-1:
            sub_sum-=arr[i]
            i+=1
    elif j==N-1: break

if min_len==float('inf'): print(0)
else: print(min_len)