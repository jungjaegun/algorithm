import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current_num = 1

for num in sequence:
    while current_num <= num:
        stack.append(current_num)
        result.append('+')
        current_num += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

for r in result:
    print(r)

