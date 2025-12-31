from collections import deque

T = int(input())
arr = deque([])
for _ in range(T):
    direction = input()

    if direction[0] == 's':
        print(len(arr))
    elif direction[0] == 'e':
        print(0 if arr else 1)
    elif direction[0] == 'f':
        print(arr[0] if arr else -1)
    elif direction[0] == 'b':
        print(arr[-1] if arr else -1)
    elif direction == 'pop':
        print(arr.popleft() if arr else -1)
    else:
        _, x = direction.split(' ')
        arr.append(int(x))