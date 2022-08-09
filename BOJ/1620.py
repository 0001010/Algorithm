n, m = list(map(int, input().split()))
dic = dict()

for i in range(1, n+1):
    x = input().rstrip()
    dic[i] = x
    dic[x] = i
    
for j in range(m):
    y = input().rstrip()
    if y.isdigit():
        print(dic[int(y)])
    else:
        print(dic[y])
