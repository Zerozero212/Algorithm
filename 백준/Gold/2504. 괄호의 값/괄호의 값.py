s = input().strip()
stack = []

for ch in s:
    if ch in '([':
        stack.append(ch)
    elif ch == ')':
        temp = 0
        while stack and stack[-1] != '(':
            if isinstance(stack[-1], int):
                temp += stack.pop()
            else:  # '['를 만나면 잘못된 괄호열
                print(0)
                exit()
        if not stack:  # '('가 없으면 잘못된 괄호열
            print(0)
            exit()
        stack.pop()  # '(' 제거
        stack.append(2 if temp == 0 else 2 * temp)
    elif ch == ']':
        temp = 0
        while stack and stack[-1] != '[':
            if isinstance(stack[-1], int):
                temp += stack.pop()
            else:
                print(0)
                exit()
        if not stack:
            print(0)
            exit()
        stack.pop()  # '[' 제거
        stack.append(3 if temp == 0 else 3 * temp)
    else:
        print(0)
        exit()

# 계산 끝나고 스택에 숫자만 남아야 함
ans = 0
for x in stack:
    if isinstance(x, int):
        ans += x
    else:
        print(0)
        exit()

print(ans)
