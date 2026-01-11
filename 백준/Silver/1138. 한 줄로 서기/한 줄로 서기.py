N = int(input())
arr = list(map(int,input().split()))
ans = [0]*N

for i in range(N):
    idx=0
    cnt=0
    while cnt <= arr[i] and idx<N:
        if not ans[idx]: 
            cnt += 1
        idx += 1
    ans[idx-1] = i+1

print(*ans)