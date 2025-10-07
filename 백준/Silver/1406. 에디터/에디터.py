import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

M = int(input())

for _ in range(M):
    command = input().rstrip()
    if command == 'L':
        if left:
            right.append(left.pop())
    elif command == 'D':
        if right:
            left.append(right.pop())
    elif command == 'B':
        if left:
            left.pop()
    else:  # 'P x'
        _, ch = command.split()
        left.append(ch)

print(''.join(left + right[::-1]))