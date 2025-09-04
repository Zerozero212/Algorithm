from itertools import combinations

def get_point(team):
    total = 0
    for x, y in combinations(team, 2):
        total += arr[x][y] + arr[y][x]
    return total

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

people = list(range(N))
min_diff = float('inf')
done=set()

for team in combinations(people, N // 2):
    if tuple(team) in done: continue
    other = [p for p in people if p not in team]
    team_score = get_point(team)
    other_score = get_point(other)
    min_diff = min(min_diff, abs(team_score - other_score))
    done.add(tuple(other))

print(min_diff)