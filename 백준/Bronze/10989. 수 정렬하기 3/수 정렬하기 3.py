N=int(input())
arr=[0]*10001
for _ in range(N):
    arr[int(input())]+=1

for i in range(1,10001):
    if arr[i]:
        for j in range(1,arr[i]+1):
            print(i)