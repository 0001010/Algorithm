import sys

n, m = map(int, sys.stdin.readline().split())
dic = dict()

for i in range(n):
    x = input().split()
    dic[x[0]] = x[1]
    
for j in range(m):
    y = input()
    print(dic[y])