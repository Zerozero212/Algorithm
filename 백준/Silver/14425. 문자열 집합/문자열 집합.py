N,M = map(int,input().split())
answer = {input() for _ in range(N)}
ans=0

for _ in range(M):
    s = input()
    if s in answer: ans+=1

print(ans)