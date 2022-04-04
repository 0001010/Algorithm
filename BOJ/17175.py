# 17175
from sys import stdin

input = stdin.readline
num = int(input())
f = [0]*(num+4)
f[0]=1
f[1]=1
f[2]=3
f[3]=5
for i in range(4, num+4):
    f[i] = (1 + f[i-1]+f[i-2])%1000000007

print(f[num])