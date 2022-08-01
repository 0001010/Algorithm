num = 1
s = []
for i in range(1,10001):
    num = i
    while True:
        if num>10000:
            break
        num = num+sum(list(map(int, str(num))))
        s.append(num)
self_num = sorted(list(set(list(range(1,10001))) - set(s)))
self_num = map(str, self_num)
print('\n'.join(self_num))