def dfs(i,sum,plus,minus,mul,div):
    global min_num,max_num
    if plus==minus==mul==div==0: 
        min_num=min(min_num,sum)
        max_num=max(max_num,sum)
        return
    if plus:
        dfs(i+1,sum+arr[i+1],plus-1,minus,mul,div)
    if minus:
        dfs(i+1,sum-arr[i+1],plus,minus-1,mul,div)
    if mul:
        dfs(i+1,sum*arr[i+1],plus,minus,mul-1,div)
    if div:
        if sum<0: dfs(i+1,(-1)*(abs(sum)//arr[i+1]),plus,minus,mul,div-1)
        else: dfs(i+1,sum//arr[i+1],plus,minus,mul,div-1)

N=int(input())
arr=list(map(int,input().split()))
plus,minus,mul,div=map(int,input().split())
min_num=float('inf')
max_num=float('-inf')
dfs(0,arr[0],plus,minus,mul,div)
print(max_num)
print(min_num)