from itertools import permutations

N, M = map(int, input().split())
result = sorted(set(permutations(sorted(list(map(int, input().split()))), M)))

for seq in result:
    print(*seq)