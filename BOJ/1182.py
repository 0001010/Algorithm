# 1182

from itertools import combinations

n, s = list(map(int, input().split()))
inputs = list(map(int, input().split()))
count = 0
for i in range(1, n+1):
    for j in combinations(inputs, i):
        if sum(j)==s:
            count+=1

print(count)