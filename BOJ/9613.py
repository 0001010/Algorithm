# 9613
# 각 조합의 gcd를 구한다음 다 더해준다 


from itertools import combinations

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a


num = int(input())
for i in range(num):
    sums = 0
    inputs = list(map(int, input().split()))[1:]
    con = combinations(inputs, 2)
    for j in con:
        sums += gcd(j[0], j[1])
    print(sums)