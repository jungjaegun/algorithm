import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = {}

for _ in range(N):
    word = input().rstrip()

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

# 길이가 M 이상의 단어들만 가져오기
filtered_words = {}

for word, count in words.items():
    if len(word) >= M:
        filtered_words[word] = count

# 정렬
sorted_words = sorted(filtered_words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, count in sorted_words:
    print(word)