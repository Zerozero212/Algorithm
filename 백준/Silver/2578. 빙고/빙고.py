from pprint import pprint
def delete(num):
    for i in range(5):
        for j in range(5):
            if arr[i][j]==num:
                arr[i][j]=0
                return

def valid():
    cnt = 0
    sol = [0,0,0,0,0]
    for i in range(5):
        if arr[i] == sol: cnt += 1
        if [row[i] for row in arr] == sol: cnt += 1
    if [arr[i][i] for i in range(5)] == sol: cnt += 1
    if [arr[i][4-i] for i in range(5)] == sol: cnt +=1
    return cnt

def find():
    for i in range(5):
        for j in range(5):
            delete(call[i][j])
            if valid() >= 3: return i*5+j+1

arr = [list(map(int,input().split())) for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]

print(find())