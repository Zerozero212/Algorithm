N,M=map(int,input().split())
arr=[0]+list(map(int,input().split()))
for i in range(1,N):
    arr[i+1]+=arr[i]
for _ in range(M):
    s,e=map(int,input().split())
    print(arr[e]-arr[s-1])