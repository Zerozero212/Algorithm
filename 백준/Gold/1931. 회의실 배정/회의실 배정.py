N=int(input())
meeting=[]
for _ in range(N):
    s,e = map(int,input().split())
    meeting.append((e,s))

meeting.sort()

cnt=0
now=0
for e,s in meeting:
    if s>=now:
        now=e
        cnt+=1

print(cnt)