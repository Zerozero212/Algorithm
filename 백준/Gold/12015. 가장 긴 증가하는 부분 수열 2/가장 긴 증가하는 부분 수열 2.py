import sys
input = sys.stdin.readline

def bin_search(target):
    l,r=0,len(ans)
    while l<r:
        mid=(l+r)//2
        if ans[mid]<target: l=mid+1
        else: r=mid
    return l

N=int(input())
arr=list(map(int,input().split()))

ans=[]

for num in arr:
    pos=bin_search(num)
    if pos == len(ans):
        ans.append(num)
    else:
        ans[pos] = num

print(len(ans))