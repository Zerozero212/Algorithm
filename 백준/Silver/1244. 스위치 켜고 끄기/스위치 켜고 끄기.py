cnt = int(input())
switch = [0] + list(map(int,input().split()))

N = int(input())
for _ in range(N):
    gender, idx = map(int,input().split())
    
    if gender == 1:
        for i in range(idx,cnt+1,idx):
            switch[i] = (switch[i] + 1) % 2
    else:
        switch[idx] = (switch[idx] + 1) % 2
        l = idx - 1
        r = idx + 1

        while l>0 and r<=cnt:
            if switch[l] != switch[r]: break
            switch[r] = (switch[r] + 1) % 2
            switch[l] = (switch[l] + 1) % 2
            l,r = l-1,r+1
    
for i in range(1,cnt+1):
    print(switch[i],end=" ")
    if i and i%20 == 0: print()