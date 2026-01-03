string = input()
bomb = input()
ans = []

for ch in string:
    ans += ch
    if ans[-1] == bomb[-1] and len(ans) >= len(bomb) and ''.join(ans[-1*(len(bomb)):]) == bomb:
        for _ in range(len(bomb)):
            ans.pop()

print(''.join(ans) if ans else "FRULA")