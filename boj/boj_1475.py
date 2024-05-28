import math

n = input()
nums = [0] * 10

for i in n:
    if i == '6' or i == '9':
        nums[6] += 0.5
    else:
        nums[int(i)] += 1

nums[6] = math.ceil(nums[6])
answer = max(nums)

print(answer)