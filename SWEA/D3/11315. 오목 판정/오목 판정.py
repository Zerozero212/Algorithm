# N>5인 경우, 주대각선(대각선의 길이가 N인 경우)를 제외하고 확인하는 방법이 잘 떠오르지 않음
def is_valid(arr, N):
    directions = [(0,1), (1,0),(1,1),(1,-1)] # 아이디어 : 0행부터 오른쪽으로 탐색하면서 'o'를 찾게 되면, (아래 / 오른쪽 / 우하단 / 좌하단)으로 탐색

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

