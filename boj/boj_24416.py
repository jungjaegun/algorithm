import sys
input = sys.stdin.readline

n = int(input())

d = [0] * (n + 1)

def fib(n):
    if n == 1 or n == 2:
        return 1

    if d[n] != 0:
        return d[n]

    d[n] = fib(n-2) + fib(n-1)
    return d[n]

def fibonacci(n):
    d[1], d[2] = 1, 1
    count = 0
    for i in range(3, n+1):
        count += 1
        d[i] = d[i-1] + d[i-2]
    return count

print(fib(n), fibonacci(n))

