T = int(input())
for trial in range(1,T+1):
    N = int(input())

    array = [list(map(int,input().split())) for _ in range(N)]
    
    max = 0
    for x in range(N):
        for y in range(N):
            # 완탐 / 해당 idx의 원소가 속한 행과 열 전체를 더한 뒤에 겹친 부분만 빼기
            temp = sum(array[x]) + sum([row[y] for row in array]) - array[x][y]
            if max < temp: max = temp
    print(f'#{trial} {max}')