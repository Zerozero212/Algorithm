import sys
input = sys.stdin.readline

N,d,k,c=map(int,input().split())
arr=[int(input()) for _ in range(N)]
ans=0
arr = arr+arr[:k-1]

for i in range(len(arr)-k+1):
    ans=max(ans,len(set(arr[i:i+k]+[c])))

print(ans)