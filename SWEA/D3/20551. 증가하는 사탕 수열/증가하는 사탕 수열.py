try_num = int(input())
for trial in range(1,try_num+1):
    a, b, c = map(int,input().split())
    candy = 0
    if c <= 2 or b <= 1:
        candy = -1
    elif b >= c:
        candy += b-c+1
        b = c-1
        if a>=b:
            candy += a-b+1
    elif b<c:
        if a>=b:
            candy += a-b+1
    print(f'#{trial} {candy}')