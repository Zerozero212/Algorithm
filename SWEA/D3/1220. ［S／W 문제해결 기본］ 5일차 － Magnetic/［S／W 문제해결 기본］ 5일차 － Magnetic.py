for try_num in range(10):
    each_try_num = int(input())
    num_list = []
    for _ in range(each_try_num):
        num_list.append(input().split())
 
    num_list = list(map(list,zip(*num_list)))
    count = 0
    for row in num_list:
        row = ''.join(row).replace('0','')
        count += row.count("12")
 
    print(f'#{try_num+1} {count}')