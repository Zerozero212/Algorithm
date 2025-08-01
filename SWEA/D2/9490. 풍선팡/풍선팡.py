total_try = int(input())
for try_num in range(total_try):
    # 행과 열 입력
    x, y = list(map(int,input().split()))
 
    array = []
    max = 0
 
    # 행 단위로 입력받기
    for row in range(x):
        array.append(list(map(int,input().split())))
 
    # 모든 원소 탐색
    for idx_x in range(x):
        for idx_y in range(y):
            value = array[idx_x][idx_y]
            sum = value
 
            for row_minus in range(1,value+1):
                if idx_x - row_minus < 0:
                    break
                sum += array[idx_x - row_minus][idx_y]
             
            for row_plus in range(1,value+1):
                if idx_x + row_plus >= x:
                    break
                sum += array[idx_x + row_plus][idx_y]
             
            for col_minus in range(1,value+1):
                if idx_y - col_minus < 0:
                    break
                sum += array[idx_x][idx_y - col_minus]
             
            for col_plus in range(1,value+1):
                if idx_y + col_plus >= y:
                    break
                sum += array[idx_x][idx_y + col_plus]
 
            if max < sum:
                max = sum
 
    print(f'#{try_num+1} {max}')