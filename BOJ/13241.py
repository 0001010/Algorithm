a, b = list(map(int, input().split()))

# gcd는 최대공약수로 유클리드 호제법으로 구현가능 a랑 b로 계속 나눠서 나머지를 b에 놓고 a자리에 b를 넣는다
# 그리고 마지막 0인 순간까지 while문 반복후 끝나면 a리턴
def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

# 최소공배수 = 두 수 곱에 gcd를 나눠주면 된다
print(int(a*b/gcd(a, b)))