N=input()
beverages = list(map(int,input().split()))
max_beverage = max(beverages)
ans=0

for beverage in beverages:
    if beverage==max_beverage:
        ans += max_beverage
        continue
    ans+=beverage/2

print(ans)