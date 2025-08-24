N,S = map(int,input().split())
arr = list(map(int,input().split()))
cnt=0
for i in range(1<<N):
    temp=[]
    for j in range(N):
        if i&(1<<j):
            temp.append(arr[j])
    if temp and sum(temp)==S: cnt+=1
print(cnt)