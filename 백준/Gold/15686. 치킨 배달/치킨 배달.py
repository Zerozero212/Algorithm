from itertools import combinations
def distance(target,home):
    sum=0
    for hx,hy in home:
        least=float('inf')
        for idx in target:
            tmp=abs(hx-chicken[idx][0])+abs(hy-chicken[idx][1])
            least=min(least,tmp)
        sum+=least
    return sum

N,M=map(int,input().split())
home=[]
chicken=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    for j in range(N):
        if tmp[j]==1: home.append((i,j))
        elif tmp[j]==2: chicken.append((i,j))

ans=float('inf')
for max_chicken in combinations(list(range(len(chicken))),M):
    ans=min(ans,distance(max_chicken,home))

print(ans)