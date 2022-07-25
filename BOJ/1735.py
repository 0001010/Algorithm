def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

one_up, one_down = list(map(int, input().split()))
two_up, two_down = list(map(int, input().split()))

down = one_down * two_down
up = one_down * two_up + one_up * two_down
gcd_num = gcd(up, down)
print(up//gcd_num, down//gcd_num)