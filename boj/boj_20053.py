import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    print(min(num_list))
    print(max(num_list))