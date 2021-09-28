x = int(input())
an = [0, 1]

for i in range(x-1):
    y = an[i]+an[i+1]
    an.append(y)

if x==0:
    print(an[0])
else:
    print(an[-1])
