import sys
input = sys.stdin.readline

def sol(i,j):
    sub_sum=arr[i]
    min_len=float('inf') 
    while i<=j<N:
        while j<N and sub_sum<S:
            j+=1
            if j==N: return min_len
            sub_sum+=arr[j]
        
        min_len=min(min_len,j-i+1)
        if i==j:
            j+=1
            if j==N: break
            sub_sum+=arr[j]
        if i<N-1:
            sub_sum-=arr[i]
            i+=1
    return min_len

N,S=map(int,input().split())
arr=list(map(int,input().split()))
ans=sol(0,0)
if ans==float('inf'): print(0)
else: print(ans)