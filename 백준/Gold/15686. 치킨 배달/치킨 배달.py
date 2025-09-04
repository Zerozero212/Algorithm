from itertools import combinations
def distance(chicken_idx_list,home):
    # chicken_idx_list : 치킨집 중 M개를 골라온 케이스 중 하나 
    # home : 집 idx 리스트
    # home에서 각 치킨 집까지의 거리 중 최솟값을 least에 저장
    # sum에다가 각 집에서 가장 가까운 치킨집까지의 거리를 더하기
    sum=0
    for hx,hy in home:
        least=float('inf')
        for idx in chicken_idx_list:
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
#치킨집의 개수가 5개이면, 5개 중에서 M개를 골라오는 경우를 확보
for max_chicken_idx_list in combinations(list(range(len(chicken))),M):
    ans=min(ans,distance(max_chicken_idx_list,home))

print(ans)