def sol():
    total = len(score)
    if new_score <= score[-1] and total >= P: return -1
    for i in range(total):
        if score[i] <= new_score:
            return i+1
    return total+1

N, new_score, P = map(int,input().split())
if N:
    score = sorted(list(map(int,input().split())),reverse=True)
    print(sol())
else:
    print(1)