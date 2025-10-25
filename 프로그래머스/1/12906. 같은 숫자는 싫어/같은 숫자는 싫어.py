def solution(arr):
    stack=[]
    for num in arr:
        while stack and stack[-1]==num:
            stack.pop()
        stack.append(num)
    return stack