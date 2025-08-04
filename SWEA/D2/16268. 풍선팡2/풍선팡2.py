T = int(input())

for trial in range(1,T+1):
    x,y = map(int,input().split())
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    array = [list(map(int,input().split())) for _ in range(x)]

    max_num = 0
    for idx_x in range(x):
        for idx_y in range(y):
            temp = array[idx_x][idx_y]
            for x_dir, y_dir in directions:
                new_x = idx_x + x_dir
                new_y = idx_y + y_dir
                if 0 <= new_x < x and 0 <= new_y < y:
                    temp += array[new_x][new_y]
            if max_num < temp: max_num = temp
    print(f'#{trial} {max_num}')
