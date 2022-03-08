# 15649
# 순열 문제는 from itertools import permutations을 활용하자

from itertools import permutations

n, m = list(map(int, input().split()))
lists = []
for i in range(1, n+1):
    lists.append(i)
per = permutations(lists, m)

for j in list(per):
    print(' '.join(list(map(str, j))))