# 2168
# 2*2에서는 최대공약수가 2이고 x+y=4이다. 생각해보면 원점을 지나서 양분되기 때문에 4-2가 되서 2가 나오고
# x = 4, y = 6일 경어 최대공약수는 2이고 x+y=10-2니까 대각선이 그려지는 정사각형의 개수는 8이 된다

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

x, y = list(map(int, input().split()))

print(x+y-gcd(x, y))