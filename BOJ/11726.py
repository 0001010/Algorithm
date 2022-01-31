# 11726
# dp문제다
#
num = int(input())
n = [0]*1001
n[1] = 1
n[2] = 2

for i in range(3, 1001):
    n[i] = n[i-1] + n[i-2]
print(n[num]%10007)