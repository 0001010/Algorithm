# 1745

from sys import stdin

num = int(stdin.readline())
lists = []

for i in range(num):
    lists.append(int(stdin.readline()))
    
lists.sort(reverse = True)
sums = 0

for j in range(1, num+1):
    if lists[j-1]-(j-1) > 0:
        sums+=lists[j-1]-(j-1)

print(sums)