import sys
input = sys.stdin.readline

T = int(input())
words = list(input().split() for _ in range(T))

for word in words:
    str = ''
    for i in range(len(word)):
        str += word[i][::-1]
        str += ' '

    print(str)