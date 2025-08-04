def is_valid(arr, N):
    directions = [(0,1), (1,0),(1,1),(1,-1)]

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':
                for dx, dy in directions:
                    count = 0
                    for k in range(5):
                        new_x = x + dx*k
                        new_y = y + dy*k
                        if 0 <= new_x < N and 0 <= new_y < N and arr[new_x][new_y] == 'o':
                            count += 1
                        else:
                            break
                    if count == 5:
                        return 1
    return 0

T = int(input())
for trial in range(1,T+1):
    N = int(input())
    array = [input() for _ in range(N)]
    result = 'YES' if is_valid(array,N) else 'NO'
    print(f'#{trial} {result}')

