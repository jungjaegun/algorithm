n = int(input())
num = n
cnt = 0
while True:
    left = num // 10
    right = num % 10
    sum = left + right

    num = (right * 10) + (sum % 10)
    cnt += 1
    if num == n:
        break

print(cnt)
