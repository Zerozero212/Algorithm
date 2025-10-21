N=int(input())
arr = sorted([int(input()) for _ in range(N)])

ans=0
for num in arr:
    ans = max(ans,len(set(i for i in range(num,num+5)) & set(arr)))

print(5-ans)