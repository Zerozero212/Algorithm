N,row,col = map(int,input().split())
arr = [list(input()) for _ in range(row)]
ans=['?']*N
for i in range(row):
    for idx in range(N*col):
        if arr[i][idx]!='?':
            ans[idx//col]=arr[i][idx]

print(''.join(ans))