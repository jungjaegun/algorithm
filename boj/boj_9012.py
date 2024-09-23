import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    words = list(input().rstrip())
    stack = []

    for word in words:
        if word == '(':
            stack.append('(')
        elif word == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break

    else:
        if not stack:
            print('YES')
        else:
            print('NO')