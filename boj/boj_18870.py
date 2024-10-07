import sys
from operator import index

input = sys.stdin.readline

def solution(N, X):

    sorted_x = sorted(set(X))

    dict = {}
    for index, number in enumerate(sorted_x):
        dict[number] = index

    result = []
    for x in X:
        result.append(dict[x])

    print(' '.join(map(str, result)))


N = int(input())
X = list(map(int, input().split()))

solution(N, X)