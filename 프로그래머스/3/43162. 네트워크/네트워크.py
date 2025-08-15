dir1=[(1,0),(-1,0),(0,1),(0,-1)]
def dfs(arr,v,x):
    v[x]=1
    for num in arr[x]:
        if not v[num]: dfs(arr,v,num)

def solution(n, computers):
    arr = []
    for i in range(n):
        temp = []
        for j in range(n):
            if computers[i][j]: temp.append(j)
        arr.append(temp)
    v=[0]*(n+1)
    answer=0
    for i in range(n):
        if not v[i]:
            dfs(arr,v,i)
            answer+=1
    return answer