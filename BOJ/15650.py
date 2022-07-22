from itertools import combinations

n, m = list(map(int, input().split()))
lists = list(range(1, n+1))

per = combinations(lists, m)
for i in per:
    print(' '.join(map(str, i)))