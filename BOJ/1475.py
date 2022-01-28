import math
N = input()
n = list(N)
counts = []
sn = 0
for i in list(n):
    if i=='6':
        sn+=1
    elif i=='9':
        sn+=1
    else:
        counts.append(n.count(i))
if len(counts)==0:
    print(math.ceil(sn/2))
else:
    if max(counts)>math.ceil(sn/2):
        print(max(counts))
    else:
        print(math.ceil(sn/2))