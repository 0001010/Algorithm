# 2331

a, p = list(map(int, input().split()))
lists = [a]
c = 0
while True:
    s = 0
    for i in list(str(a)):
        s+=int(i)**p
    if s in lists:
        break
    else:
        a = s
        lists.append(s)
for i in lists:
    if i==s:
        break
    else:
        c+=1
print(c)