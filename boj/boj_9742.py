import sys
from itertools import permutations

input = sys.stdin.readline

while True:
    user_input = input().rstrip()

    if user_input == '':  # 빈 줄 처리
        break

    string, number = user_input.split()
    number = int(number)

    string_list = list(string)
    result_list = list(permutations(string_list))

    if number <= len(result_list):
        answer = ''.join(result_list[number - 1])
    else:
        answer = "No permutation"

    print(f"{string} {number} = {answer}")

