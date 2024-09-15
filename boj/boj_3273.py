import sys
input = sys.stdin.readline

n = int(input())
sequence = (list(map(int, input().split())))
x = int(input())

# 정렬
sequence.sort()

# 투포인터
# 1. 시작점(start)와 끝점(end)이 첫번째 원소의 인덱스를 가리키도록 한다
# 2. 현재 부분 합(interval_sum)이 M과 같다면, 카운트한다.
# 3. 현재 부분 합(interval_sum)이 M보다 작다면, end를 +1 한다.
# 4. 현재 부분 합(interval_sum)이 M보다 크거나 같다면, start를 +1 한다.
# 5. 모든 경우의 수를 확인할 때까지 2~4를 반복한다.

# 이 문제 접근
# 1. 오름차순 정렬
# 2. 포인터 설정 : 첫 번쨰 포인터는 수옆의 맨앞(시작점), 마지막 포인터는 수열의 맨끝(끝점)
# 3. 합 계산 : 두 포인터가 가르키는 값이 x랑 같은지 체크. 합이 x보다 크면 끝점을 왼쪽으로 이동. 합이 x보다 작으면 시작점을 오른쪽으로 이동. 같으면 둘다 이동

# 정답 변수
count = 0
start = 0
end = n - 1
current_sum = 0

# start를 차례대로 반복하면서 증가
while start < end:
    current_sum = sequence[start] + sequence[end]

    if current_sum == x:
        count += 1
        start += 1
        end -= 1
    elif current_sum < x:
        start += 1
    elif current_sum > x:
        end -= 1

print(count)