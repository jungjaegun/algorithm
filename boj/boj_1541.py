import sys
input = sys.stdin.readline

data = input().rstrip().split('-')

result = []
for d in data:
    dd = map(int, d.split('+'))
    result.append(sum(dd))

answer = result[0]
for i in range(1, len(result)):
    answer -= result[i]

print(answer)