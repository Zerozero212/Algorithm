def solution(m, n, puddles):
    arr=[[0]*m for _ in range(n)]
    for j,i in puddles:
        arr[i-1][j-1]=-1
    arr[0][0]=1

    for i in range(n):
        for j in range(m):
            if arr[i][j]==-1: continue
            for di,dj in [(-1,0),(0,-1)]:
                ni,nj=i+di,j+dj
                if 0<=ni and 0<=nj and arr[ni][nj]!=-1: 
                    arr[i][j]+=arr[ni][nj]
                arr[i][j]%=(10**9+7)
    return arr[n-1][m-1]