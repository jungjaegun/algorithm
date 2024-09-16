import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    word = str(input())
    print(word[0]+word[-2])
