N=int(input())
triangle = [list(map(int,input().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(len(triangle[i])):
        tmp=[]
        prev_len = len(triangle[i-1])
        for idx in (j-1,j):
            if 0<=idx<prev_len:
                tmp.append(triangle[i-1][idx])
        triangle[i][j] += max(tmp)

print(max(triangle[N-1]))