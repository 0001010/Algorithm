# 2609
# 최대공약수와 최소공배수
# gcd 연습하기 좋은 문제

one, two = list(map(int, input().split()))

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a
g = gcd(one, two)
print(g)
print((one*two)//g)