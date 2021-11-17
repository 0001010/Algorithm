x = int(input())
lists = [0, 1]
for i in range(x-2):
    a = lists[i]+lists[i+1]
    lists.append(a)
print(lists[-1]+lists[-2])