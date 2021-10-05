n, m = list(map(int, input().split()))

change = 0
re = []

for i in range(m):
    card = list(map(int, input().split()))
    if card[0]>=n:
        change+=1
    else:
        re.append(card)

if change>=m-1:
    print(0)
else:
    res = []
    for w in re:
        res.append(n - w[0])
    res.sort()
    print(sum(res[:m-change-1]))

