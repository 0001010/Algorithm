# 제로 10773
from sys import stdin

k = int(stdin.readline())
lists = []

for i in range(k):
    num = int(stdin.readline())
    if num==0:
        lists.pop()
    else:
        lists.append(num)
print(sum(lists))
