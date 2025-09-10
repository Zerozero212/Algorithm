def sol(i,j):
    ans=float('inf')
    while j<N:
        while j<N:
            tmp=arr[j]-arr[i]
            if tmp<M: j+=1
            elif tmp==M: return M
            else:
                ans=min(ans,tmp)
                break
        i+=1
    return ans

N,M=map(int,input().split())
arr=sorted([int(input()) for _ in range(N)])
print(sol(0,1))