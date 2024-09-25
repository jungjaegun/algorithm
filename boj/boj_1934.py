import math

import sys
input = sys.stdin.readline

T = int(input())

def solution_1(T):
    for _ in range(T):
        A, B = map(int, input().split())
        print(math.lcm(A, B))

# solution_1(T)

# 최소공배수 = A * B / 최대공약수(math.gcd)
def solution_2(T):
    for _ in range(T):
        A, B = map(int, input().split())
        print(int(A * B // math.gcd(A, B)))

solution_2(T)
