N = int(input())
arr = list(map(int,input().split()))
ans = [0] * N

for i in range(N-1):
    curr = arr[i+1] - arr[i]
    ans[i] += 1
    ans[i+1] += 1
    for j in range(i+2,N):
        grad = (arr[j] - arr[i]) / (j-i)
        if grad > curr: 
            ans[i] += 1
            ans[j] += 1
            curr = grad

print(max(ans))