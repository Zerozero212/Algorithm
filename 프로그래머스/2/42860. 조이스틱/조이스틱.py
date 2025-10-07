def solution(name):
    N = len(name)
    vertical = 0
    for ch in name:
        diff = ord(ch) - ord('A')
        vertical += min(diff, 26 - diff)

    move = N - 1
    # name = 'BABBAAABBABB'라고 하면, BABB / AAA / BBABB로 나눠보자.
    # idx가 3인 B와 idx7인 B까지는 도달해야 함.
    for i in range(N):
        nxt = i + 1
        while nxt < N and name[nxt] == 'A':
            nxt += 1
        move = min(move, 2 * i + N - nxt, i + 2 * (N - nxt))

    return vertical + move