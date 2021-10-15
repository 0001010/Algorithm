num = int(input())
keys = []
values = []

for i in range(num):
    x=input().split()
    keys.append(x[0])
    values.append(x[1])
print(keys[values.index(min(values))])
