import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    x -= 1
    y -= 1

    found = False
    for i in range(x, M * N, M):
        if i % N == y:
            print(i + 1)
            found = True
            break

    if not found:
        print(-1)
