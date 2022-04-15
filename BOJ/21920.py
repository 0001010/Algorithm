# 21920
# 서로소는 두 수의 최대공약수가 1인 수를 말한다.
# gcd를 구해서 1이 되는 것들의 평균을 구하면 된다.

num = int(input())
a = list(map(int, input().split()))
x = int(input())

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

count = 0
sums = 0

for i in a:
    if gcd(i, x)==1:
        sums += i
        count += 1

print("{:.6f}".format(sums/count))