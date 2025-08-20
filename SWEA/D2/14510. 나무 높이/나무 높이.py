T = int(input())
for t in range(1, T + 1):
    N = int(input())
    tree_arr = list(map(int, input().split()))
    tree_max = max(tree_arr)
    tt_df = 0  
    odd = 0

    for h in tree_arr:
        df = tree_max - h
        tt_df += df
        odd += df % 2
    
    days = (tt_df // 3) * 2 + (tt_df % 3)
    one_count = (days + 1) // 2
    
    if odd > one_count: days = 2 * odd - 1
    
    print(f'#{t} {days}')