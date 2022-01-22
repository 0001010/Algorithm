from sys import stdin

input = stdin.readline

num = int(input())
lists = []

for i in range(num):
    lists.append(int(input()))

lists.sort()
sums = 0

for j in range(1, num+1):
    sums += abs(lists[j-1] - j)

print(sums)
