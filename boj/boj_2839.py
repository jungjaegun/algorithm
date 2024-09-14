import sys
input = sys.stdin.readline

N = int(input())

def greedy(sugar):
    # 정답 변수
    count = 0
    while sugar >= 0:
        # 5로 정확하게 나눌 수 없으면
        if sugar % 5 == 0:
            count += sugar // 5
            print(count)
            break

        # 5로 정확하게 나뉘지 않으면 3을 하나씩 빼서 5로 나눠질때까지 반복문을 돌린다
        # 예를 들어 18이면 일단 5로 안 나뉘기 때문에 3을 뺴주고 count를 1을 더해준다음에 다시 돌아가면 5로 나뉜다
        sugar -= 3
        count += 1
    else:
        print(-1)

def bruteforce(sugar):
    # 5kg 봉지를 가장 많이 사용해본다
    min_count = float('inf')
    for five_count in range(sugar // 5 + 1): # 21인 경우 0부터 4까지
        remain_sugar = sugar - (5 * five_count)
        if remain_sugar % 3 == 0:
            three_count = remain_sugar // 3
            current_count = three_count + five_count
            min_count = min(min_count, current_count)

    if min_count == float('inf'):
        print(-1)
    else:
        print(min_count)

bruteforce(N)