N=int(input())

if N==0 or N==1: print(1)
else:
    std=1
    for i in range(1,N+1):
        std*=i
    print(std)