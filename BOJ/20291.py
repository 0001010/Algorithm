from collections import Counter

num = int(input())
lists = []

for i in range(num):
    inputs = input().split('.')
    lists.append(inputs[1])

counts = Counter(lists)
a = sorted(counts.items(), key = lambda item : item[0])

for j in a:
    z = list(map(str, j))
    print(' '.join(z))
