num = int(input())

lists = []

for i in range(num):
    lists.append(int(input()))
if max(lists)<3:
    f = [0]*4
else:
    f = [0]*(max(lists)+1)
f[0] = 1
f[1] = 1

for j in range(2, max(lists)+1):
    f[j] = f[j-1] + f[j-2]
    
for l in lists:
    if l==0:
        print(1, 0)
    elif l==1:
        print(0, 1)
    else:
        print(f[l-2],f[l-1])