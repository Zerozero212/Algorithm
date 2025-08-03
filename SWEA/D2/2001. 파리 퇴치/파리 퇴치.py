try_num = int(input())
for trial in range(1,try_num+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0

    for idx_x in range(N-M+1):
        for idx_y in range(N-M+1):
            temp = [arr[x][y] for x in range(idx_x, idx_x+M) for y in range(idx_y,idx_y+M)]
            if max < sum(temp):
                max = sum(temp)
    print(f'#{trial} {max}')