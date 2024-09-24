import sys
import math
input = sys.stdin.readline

T = int(input())

# 최대공약수 구하는 공식 = math.gcd
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a

# 최대공약수 함수를 통해 최소공배수를 구하는 공식
def lcm(a, b):
    return int((a * b) / gcd(a, b))

for _ in range(T):
    A, B = map(int, input().split())
    print(lcm(A, B))

