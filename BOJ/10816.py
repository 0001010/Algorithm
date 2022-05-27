# 10816
from collections import Counter

one = int(input())
input_one = list(map(int, input().split()))
two = int(input())
input_two = list(map(int, input().split()))

counts = Counter(input_one)
for i in input_two:
    if i in counts:
        print(counts[i], end = ' ')
    else:
        print(0, end = ' ')