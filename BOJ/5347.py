# 5347
# gcd이용문제 어렵지 않게 풀면된다.

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

num = int(input())
for i in range(num):
    a, b = list(map(int, input().split()))
    g = a*b//gcd(a, b)
    print(g)
    