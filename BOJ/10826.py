num = int(input())
lists = [0, 1]
for i in range(num-1):
    lists.append(lists[i]+lists[i+1])

if num==0:
    print(lists[0])
else:
    print(lists[-1])
