def solution(numbers):
    max = numbers[0]*numbers[1]
    for idx in range(len(numbers)):
        for idx_2 in range(len(numbers)):
            if idx==idx_2:
                continue
            temp = numbers[idx]*numbers[idx_2]
            if max < temp:
                max = temp
    return max