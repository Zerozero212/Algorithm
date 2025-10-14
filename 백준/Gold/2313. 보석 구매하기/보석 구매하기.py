N=int(input())
jewel_cnt = [0]*N
jewel_price = []
for n in range(N):
    jewel_cnt[n]=int(input())
    jewel_price.append(list(map(int,input().split())))

total = [-1e9]*N
idx = [(0,0) for _ in range(N)]

for n in range(N):
    for l in range(jewel_cnt[n]):
        sub_total=jewel_price[n][l]
        if sub_total>total[n]:
                total[n]=sub_total
                idx[n]=(l,l)
        elif sub_total==total[n]:
            if idx[n][1]-idx[n][0]>0:
                idx[n]=(l,l)
        for r in range(l+1,jewel_cnt[n]):
            sub_total+=jewel_price[n][r]
            if sub_total>total[n]:
                total[n]=sub_total
                idx[n]=(l,r)
            elif sub_total==total[n]:
                if idx[n][1]-idx[n][0]>r-l:
                    idx[n]=(l,r)

print(sum(total))
for l,r in idx:
    print(l+1,r+1)