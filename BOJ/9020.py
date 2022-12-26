# 9020
# 에라토스테네스의 체로 입력수중 가장 큰 수를 넣는다.
# for문으로 입력 수를 불러와서 절반으로 나눈다음 두 수가 모두 True가 될때까지 첫번째는 -1 두번째는 +1을 하면서 계산해주면 된다.

from collections import deque

def prime(n):
    s = [True]*(n+1)
    m = int((n+1)**0.5)
    for i in range(2, m+1):
        if s[i]==True:
            for j in range(i+i, n+1, i):
                s[j]=False
    return s

max_x = 0
num = int(input())
lists = deque()
for i in range(num):
    x = int(input())
    if max_x<=x:
        max_x = x
    lists.append(x)

prime_x = prime(max_x)

for j in lists:
    one = j//2
    two = one
    for z in range(len(prime_x)):
        if prime_x[one] and prime_x[two]:
            print(one, two)
            break
        one -= 1
        two += 1