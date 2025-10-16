N=int(input())
P = list(map(int,input().split()))
P.sort()

time=0
for i in range(1,N+1):
    time += P[i-1]*(N-i+1)

print(time)