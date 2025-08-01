try_num = int(input())
for trial in range(1,try_num+1):
    N, M = map(int,input().split())
    arr = []
    max = 0
    for n in range(N):
        arr.append(list(map(int,input().split())))
 
    for idx_x in range(N-M+1):
        for idx_y in range(N-M+1):
            temp = 0
            for sub_idx_x in range(M):
                for sub_idx_y in range(M):
                    temp += arr[idx_x+sub_idx_x][idx_y+sub_idx_y]
            if max < temp:
                max = temp
    print(f'#{trial} {max}')