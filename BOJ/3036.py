n = int(input())

rings_len = list(map(int, input().split()))

def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

for i in range(1, n):
    gcd_div = gcd(rings_len[i], rings_len[0])
    print(str(rings_len[0]//gcd_div) + '/' + str(rings_len[i]//gcd_div))