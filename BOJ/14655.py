x = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
seconde = []
first = list(map(abs, first))
for i in second:
    if i>0:
        b = -i
        seconde.append(b)
    else:
        seconde.append(i)
print(sum(first)-sum(seconde))
