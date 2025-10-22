coor = [[0]*100 for _ in range(100)]

for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            coor[i][j]+=1

ans=10**4
for row in coor:
    ans -= row.count(0)

print(ans)