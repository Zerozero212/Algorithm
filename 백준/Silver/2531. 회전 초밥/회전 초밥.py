N,d,k,c=map(int,input().split())
arr=[]
ans=0
for _ in range(N):
    arr.append(int(input()))
arr = arr+arr[:k-1]

for i in range(len(arr)-k+1):
    ans=max(ans,len(set(arr[i:i+k]+[c])))

print(ans)