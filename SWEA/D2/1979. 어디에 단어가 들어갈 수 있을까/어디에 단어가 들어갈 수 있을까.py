total_try = int(input())
for trial in range(1,total_try+1):
    N, k = map(int, input().split())
    array = []
    k_count = 0
    for row in range(N):
        array.append(input().split())
 
    new_array = list(map(list,zip(*array)))
 
    array_list = [array, new_array]
 
    for array_component in array_list:
        for row in array_component:
            new_row = ''.join(row)
            new_row = new_row.split('0')
            for new_row_component in new_row:
                if len(new_row_component) == k:
                    k_count += 1
 
    print(f'#{trial} {k_count}')