import sys
input = sys.stdin.readline

N = int(input())
students = list(input().rstrip() for _ in range(N))

# 브루트 포스
for i in range(len(students[0])):
    numbers = []
    for student in students:
        numbers.append(student[-1-i:])

    if len(numbers) == len(set(numbers)):
        print(len(numbers[0]))
        break