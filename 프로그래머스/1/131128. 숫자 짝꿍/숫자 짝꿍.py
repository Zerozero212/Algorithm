from collections import Counter

def solution(X, Y):
    countX = Counter(X)
    countY = Counter(Y)

    result = []
    for digit in map(str, range(9, -1, -1)):  
        common = min(countX[digit], countY[digit])
        result.append(digit * common)

    answer = ''.join(result)

    if not answer:   
        return "-1"
    if answer[0] == "0":  
        return "0"
    return answer