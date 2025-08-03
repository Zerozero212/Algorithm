def is_valid_sudoku(board):
    s = set(range(1, 10))

    # 가로 & 세로 체크
    for i in range(9):
        if set(board[i]) != s: return False
        if set(row[i] for row in board) != s: return False

    # 3x3 서브그리드 체크
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            block = [board[i][j] for i in range(x, x + 3) for j in range(y, y + 3)]
            if set(block) != s: return False

    return True

T = int(input())
for t in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    result = 1 if is_valid_sudoku(board) else 0
    print(f'#{t} {result}')