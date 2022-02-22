# 10974
# 순열문제는 permutations로 풀기!

from itertools import permutations
num = int(input())

per = permutations(list(range(1, num+1)), num)

for i in per:
    print(' '.join(list(map(str, i))))