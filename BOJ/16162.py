n, a, d = list(map(int, input().split()))
lists = list(map(int, input().split()))
count = 0

for i in lists:
    if i==a:
        a+=d
        count+=1

print(count)