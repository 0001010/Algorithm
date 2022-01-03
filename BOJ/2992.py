# 2992
# 순열과 조합 문제에서 itertools를 활용하자
from itertools import permutations

x = input()
lists = []

for i in permutations(list(x), len(list(x))):
    a = int(''.join(list(i)))
    if a>int(x):
        lists.append(a)

lists.sort()

if len(lists)==0:
    print(0)
else:
    print(int(lists[0]))