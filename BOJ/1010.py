num = int(input())

for i in range(num):
    n, m = list(map(int, input().split()))
    up = 1
    down = 1
    for j in range(min(n,m)):
        up*=(max(n,m)-j)
        down *= j+1
    print(int(up/down))