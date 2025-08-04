T = int(input())
# directions을 활용해서 8개 구간 탐색
for trial in range(1,T+1):
    x,y = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(x)]

    directions = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
    result = 0

    for idx_x in range(x):
        for idx_y in range(y):
            count = 0
            for dx,dy in directions:
                new_x = idx_x + dx
                new_y = idx_y + dy
                if 0 <= new_x < x and 0 <= new_y < y and array[idx_x][idx_y] > array[new_x][new_y]: count += 1
            if count >= 4: result += 1
    print(f'#{trial} {result}')